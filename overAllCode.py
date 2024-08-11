import csv
from datetime import datetime

# with open('ICICI-Input-Case2.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
#     rows = list(csv_reader)
    
# with open('HDFC-Input-Case1.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
#     rows = list(csv_reader)

# with open('IDFC-Input-Case4.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
#     rows = list(csv_reader)

# with open('Axis-Input-Case3.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
#     rows = list(csv_reader)


def checkWheaterItisPersonOrtransaction(incomingRow):
    # Extra code for the Removing NAN or NULL Values
    transactionType = ""
    nameOfPerson = ""
    for j in range(len(incomingRow)):
        if (str(incomingRow[j]).strip() == '') or (str(incomingRow[j]) == "NAN") or (str(incomingRow[j]) == "ï»¿"):
            continue
        goodlist.append(incomingRow[j].strip())  
    
    # Now We Got the Good List so we need to Correct it
    # Assigning the nameof person and transaction type
    
    if len(goodlist) == 1:
        subList = goodlist[0].split(' ')
        if len(subList) == 2:
            if subList[1] == "Transactions" or subList[1] == "Transaction":
                transactionType = subList[0]
        else:
            nameOfPerson = subList[0]
    return [transactionType,nameOfPerson]

def extract_transaction_name_and_city(transaction):
    parts = transaction.rsplit(',', 1)[0].strip().split()
    
    city = parts[-1] if parts else None
    transaction_name = " ".join(parts[:-1]) if len(parts) > 1 else None
    
    return transaction_name, city

def extract_transaction_name_city_currency(line):
    parts = line.strip().split()
    currency = ""
    city = ""
    transaction_name = ""
    
    if parts and len(parts) >= 2:
        currency = parts[-1]
        city = parts[-2]
        transaction_name = parts[0:-2]
        transaction_name = " ".join(transaction_name)

    return transaction_name, city, currency

def check_date_format(date_str):
    date_str = date_str.strip()
    
    if len(date_str) != 8:
        return False
    
    if date_str[2] != '-' or date_str[5] != '-':
        return False
    
    day = date_str[:2]
    month = date_str[3:5]
    year = date_str[6:]
    
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    
    day = int(day)
    month = int(month)
    year = int(year)
    
    if day < 1 or day > 31:
        return False
    if month < 1 or month > 12:
        return False
    if year < 0 or year > 99:
        return False
    
    return True

def convert_date_format(date_str):
    try:
        # Try parsing the date assuming it's in MM-DD-YYYY format
        return datetime.strptime(date_str, "%m-%d-%Y").strftime("%d-%m-%Y")
    except ValueError:
        # If parsing fails, it's already in DD-MM-YYYY format
        return date_str

input_files = [
    'ICICI-Input-Case2.csv',
    'HDFC-Input-Case1.csv',
    'IDFC-Input-Case4.csv',
    'Axis-Input-Case3.csv'
]    

output_rows = [["Date", "Transaction Description", "Debit", "Credit", "Currency", "CardName", "Transaction", "Location"]]
mySet = {"Date", "Transaction Description", "Debit", "Credit", "Currency", "CardName", "Transaction", "Location","Amount","Transaction Details"}
dict = {}

for input_file in input_files :
    with open(input_file, mode='r') as file:
        rows = list(csv.reader(file))
    
    resultOfSingleFile = [["Date", "Transaction Description", "Debit", "Credit", "Currency", "CardName", "Transaction", "Location"]]    
        
    for i in range(len(rows)):
        
        incomingRow = rows[i]
        goodlist = []
        headerPostion = {}
        currency = "INR"
        #  Now Assigning the which coloumns are present at which location
        # This will give me the name of the person and whcih type of transaction are going.... 
        
        output1,output2 = checkWheaterItisPersonOrtransaction(incomingRow=incomingRow)
        
        if output1 != '' and output2 == '':
            transactionType = output1 
        if output2 != '' and output1 == '':
            nameOfPerson = output2 
            
        # Below code  will gernate the unqiue fields that are present in the dataset and according to it append it .
        
        count = 0
        for i in range(len(incomingRow)):
            if incomingRow[i].strip() in mySet:
                count= count + 1
                dict[incomingRow[i].strip()] = i
        if count != 0:
            continue
        if len(dict) == 0:
            continue

        creditAmount = 0
        debitAmount = 0
        city = ''
        transactionDes = ""

        if 'Debit' in dict:
            idx = dict['Debit']
            debitAmount = incomingRow[idx]
            
        if 'Credit' in dict :
            idx = dict['Credit']
            creditAmount = incomingRow[idx]
            
        if 'Amount' in dict and (len(incomingRow) > dict["Amount"]):
            idx = dict['Amount']
            amount = incomingRow[idx]
            amount = amount.strip()
            temp = amount.split(" ")
            
            if len(temp) == 1 and temp[0] == '':
                continue
            getEntites = []
            
            for j in range(len(temp)):
                if (str(temp[j]).strip() == ''):
                    continue
                getEntites.append(temp[j].strip()) 
            if len(getEntites) == 2 and ((getEntites[1] == 'cr') or (getEntites[1] == 'Cr') or getEntites[1] == 'cR'):
                creditAmount = getEntites[0]
                debitAmount = 0
            else :
                creditAmount = 0
                debitAmount = getEntites[0]    
        
        if "Transaction Description" in dict :
            transactionDes = incomingRow[dict["Transaction Description"]]
        if "Transaction Details" in dict :
            transactionDes = incomingRow[dict["Transaction Details"]]
            
        
        
        if "Transaction Description" in dict or "Transaction Details" in dict:
            if transactionType == "Domestic":
                if "Transaction Description" in dict :
                    transactionDes,city = extract_transaction_name_and_city(incomingRow[dict["Transaction Description"]])
                else :
                    transactionDes,city = extract_transaction_name_and_city(incomingRow[dict["Transaction Details"]])
            else :
                if "Transaction Description" in dict :
                    transactionDes,city,currency = extract_transaction_name_city_currency(incomingRow[dict["Transaction Description"]])
                else :
                    transactionDes,city,currency = extract_transaction_name_city_currency(incomingRow[dict["Transaction Details"]])
        
    
        # print("For a Person name - ",nameOfPerson," and Transaction Type is ",transactionType,"Debited Amount - ",debitAmount," and ","Credit Amount" ,creditAmount, "and the transaction Description will be ",transactionDes)
        
        nameOfPerson = nameOfPerson.strip()
        if nameOfPerson == '' or nameOfPerson == str(None) or nameOfPerson == None:
            continue
        transactionDes = str(transactionDes).strip()
        if transactionDes == '' or transactionDes == str(None) or transactionDes == None:
            continue
        transactionType = transactionType.strip()
        if transactionType == '' or transactionType == str(None) or transactionType == None:
            continue
        city = city.strip()
        if city == '' or city == None or city == str(None):
            continue  
        
        date = incomingRow[dict["Date"]]        
        date = convert_date_format(date)
        output_rows.append([date,str(transactionDes).strip(),debitAmount,creditAmount,currency,nameOfPerson,transactionType,city])
        resultOfSingleFile.append([date,str(transactionDes).strip(),debitAmount,creditAmount,currency,nameOfPerson,transactionType,city])
        with open(input_file.split('-')[0] + "-output.csv" , mode='w', newline='') as file:
            writer = csv.writer(file)

            for row in resultOfSingleFile:
                writer.writerow(row)
        
    dict.clear()
            

filename = "step1.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    for row in output_rows:
        writer.writerow(row)

# print(output_rows)


# Parse the Date and Sort

def parse_date(date_str):
    day, month, year = map(int, date_str.split('-'))
    return (year, month, day)

def sort_csv_by_date(data):
    header = data[0]
    rows = data[1:]
    
    sorted_rows = sorted(rows, key=lambda row: parse_date(row.split(',')[0]))
    return [header] + sorted_rows

input_filename = "step1.csv"
output_filename = "OverAllOutput.csv"

with open(input_filename, mode='r') as infile:
    lines = infile.readlines()
    
    # print(lines)

    if lines:
        header = lines[0]
        data = lines[1:]
    
    sorted_data = sort_csv_by_date([header] + data)

    with open(output_filename, mode='w', newline='') as outfile:
        for row in sorted_data:
            outfile.write(row)

print("Sorted data has been written to", output_filename)
            






            
            
        
        
        

    
    
    
    
    
            

    
    
    




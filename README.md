Rahul has multiple credit cards of different banks and each of these banks generate card 
statements in different formats. To analyze his statements, Rahul needs our help to 
standardize them in a single format. To help Rahul, we need to write logic that can normalize 
any statement in a standard format. Take reasonable assumptions and make the logic as 
generic as possible.
Function signature to be implemented:-
- StandardizeStatement( inputFile, outputFile)
Following key points need to be considered: -
 Convert Date to DateTime format before printing in standard CSV and account for DDMM-YYYY, MM-DD-YYYY and DD-MM-YY format
 Convert the Amount to Double
 A single Input file should be taken at a time as a parameter and output file should be
generated for the same. (Input/Output files should not be merged)
 While submitting the code, please attach all the four output files
 The output file name should be as per input file name. (Example of Input and output
filename convention is given below for reference)
exampleInputFile : HDFC-Input-Case1.csv
OutputFile : HDFC-Output-Case1.csv
Attached are 4 input test case files and the Standard Format CSV. Feel free to reach us in case


RAW CSV DATA - 
,,Domestic Transactions,
"Date      ",Debit,Credit,Transaction Details
,,Rahul,
,,,
28-01-2018,1099,,INDIAN RAILWAY CATERINGNEW DELHI
28-01-2018,34980,,FLIPKART INTERNET PRIVA BANGALORE
28-01-2018,660,,TIPSY CATERERS JAIPUR
29-01-2018,57181,,MAKEMYTRIP INDIA PVT LT NEWDELHI
29-01-2018,,3390,INDIAN RAILWAY CATERING NEWDELHI
29-01-2018,,53326,MAKEMYTRIP INDIA PVT LT NEWDELHI
30-01-2018,,680,INDIAN RAILWAY CATERING NEWDELHI
,,,a
"Date      ",Debit,Credit,Transaction Details
,,Ritu,
,,,
22-02-2018,,1845,FEETOES GURGAON
18-02-2018,949,,DECATHLON SPORTS INDIA GURGAON
09-02-2018,1250,,SILVER GALERIE A UNIT    GURGAON
23-02-2018,,1650,DNA PHARMACY           GURUGRAM
26-02-2018,,413,MONTE CARLO            GURGAON
27-02-2018,,456,THE ROOM               GURGAON
27-02-2018,1938,,LITTLE BURGUNDY        GURGAON
,,,
,,,



Output CSV Data - 

Date,Transaction Description,Debit,Credit,Currency,CardName,Transaction,Location
28-01-2018,INDIAN RAILWAY CATERINGNEW,1099,,INR,Rahul,Domestic,DELHI
28-01-2018,FLIPKART INTERNET PRIVA,34980,,INR,Rahul,Domestic,BANGALORE
28-01-2018,TIPSY CATERERS,660,,INR,Rahul,Domestic,JAIPUR
29-01-2018,MAKEMYTRIP INDIA PVT LT,57181,,INR,Rahul,Domestic,NEWDELHI
29-01-2018,INDIAN RAILWAY CATERING,,3390,INR,Rahul,Domestic,NEWDELHI
29-01-2018,MAKEMYTRIP INDIA PVT LT,,53326,INR,Rahul,Domestic,NEWDELHI
30-01-2018,INDIAN RAILWAY CATERING,,680,INR,Rahul,Domestic,NEWDELHI
22-02-2018,FEETOES,,1845,INR,Ritu,Domestic,GURGAON
18-02-2018,DECATHLON SPORTS INDIA,949,,INR,Ritu,Domestic,GURGAON
02-09-2018,SILVER GALERIE A UNIT,1250,,INR,Ritu,Domestic,GURGAON
23-02-2018,DNA PHARMACY,,1650,INR,Ritu,Domestic,GURUGRAM
26-02-2018,MONTE CARLO,,413,INR,Ritu,Domestic,GURGAON
27-02-2018,THE ROOM,,456,INR,Ritu,Domestic,GURGAON


SENG8080

## Contributors
1. Vishalbhai Barvaliya
2. Sumukh Dhawade
3. Sindhu Parkavi Sivakumar
4. Kevin Jacob Mathew
5. Lakshay Soni
6. Jose Jaramillo
7. Jeevan Preet Saini
8. Mansi Trivedi
9. Amandeep Amandeep
10. Yusra Khan:)
11. Garima Sharma
12. Mukesh Yarlagadda
13. Nisha Kathiriya
14. Arman Fidaulla Sharief
15. Kriti Thamman
16. Hareesh Varatharaj
17. Prathmesh Jani
18. Sagar Vaiyata
19. Darshan Lunagariya
20. Karan Sorathiya
21. Prashant Thakkar
22. Roopesh Votarikari
23. Chandan Sulimalthe Sannappa
24. Pradeep Gahlawat
25. Mrunal Wavdhane
26. Sree Kodavanti
27. Zarana Gohil
28. Karan Patel

## data collection using Python script 

data_collection_from_s3.py - This script can be used to retrieve the data and unzip the files recursively through all the folders.

## data Collection using PowerShell script

## Prerequisite
1. Install 7zip
2. Install AWS CLI

## To Run the file
1. Use power shell
2. Navigate to your file folder
3. use command  .\Data_Collection_From_AWS_S3.ps1 to run the file

## Script Explanation

1. It Creates a folder 'genome_browser' if it doesn't exist
2. Collects all the objects under the aws s3 folder and store them in the object field
3. Iterate through the objects one by one and download them from aws s3 to the local folder
4. Get all the .gz files from the local folder
5. Iterate through all the .gz files and unzip them in the destination folder using 7zip commands

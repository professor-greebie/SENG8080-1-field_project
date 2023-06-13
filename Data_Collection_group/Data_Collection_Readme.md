## data Collection - Readme.md

## Prerequisite
1. Install 7zip
2. Install AWS CLI

## To Run the file
1. Use power shell
2. Navigate to your file folder
3. use command  .\Data_Collection_From_AWS_S3.ps1 o run the file

## Script Explanation

1. It Create a folder 'genome_browser', if it doesnt exists
2. Collects all the objects under the aws s3 folder and store it in object field
3. Iterate through the objects one by one and download it from aws s3 to the local folder
4. Get all the .gz files from the local folder
5. Iterate through all the .gz files and unzip them in the destination folder using 7zip commands
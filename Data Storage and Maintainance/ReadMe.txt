Instructions for the DevOps Team:

Ensure MongoDB is Installed and Running:
Make sure MongoDB is installed and running on the server where you'll run the script. If not, follow MongoDB's official installation guide for your platform.

Install Required Libraries:
Install the required pymongo library using the following command:

pip install pymongo

Prepare CSV File:
Place your CSV file in a location accessible to the script.

Modify the Script Inputs:
Open the store_data_in_mongo.py script in a text editor and provide the following information:

Replace 'path/to/your/csv/file.csv' with the actual path to your CSV file.
Replace 'your_database_name' with the desired database name.
Replace 'your_collection_name' with the desired collection name.

Run the Script:
Open a terminal and navigate to the directory containing the script. Run the script using the following command:

python store_data_in_mongo.py

Verify Data in MongoDB:
Connect to your MongoDB server and verify that the data has been inserted into the specified database and collection.





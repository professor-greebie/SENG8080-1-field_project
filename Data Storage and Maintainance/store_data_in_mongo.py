import csv
from pymongo import MongoClient

def store_csv_data_in_mongo(csv_file_path, db_name, collection_name, mongo_uri='mongodb://localhost:27017/'):
    try:
        # Connect to MongoDB
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]

        # Read CSV and insert data into MongoDB
        with open(csv_file_path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                collection.insert_one(row)

        print("Data inserted successfully!")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the MongoDB connection
        if client:    #To ensure that the MongoDB connection is closed only if it was successfully established in the first place
            client.close()

# Provide the necessary inputs
csv_file_path = 'path/to/your/csv/file.csv' #replace it with your path
db_name = 'your_database_name' # Replace it with your DB 
collection_name = 'your_collection_name' # Replace it with your collection name

store_csv_data_in_mongo(csv_file_path, db_name, collection_name)

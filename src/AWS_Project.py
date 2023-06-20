import subprocess
import json
import os
import gzip
import sys

bucket_name = "genome-browser"
s3_folder_key = "goldenPath/wuhCor1/bigZips"

if len(sys.argv) >= 2:
    local_folder = sys.argv[1]
else:
    local_folder = "C:/genome-browser/"

# Create the local folder if it doesn't exist
if not os.path.exists(local_folder):
    os.makedirs(local_folder)

# List objects in the S3 folder
list_objects_command = [
    "aws", "s3api", "list-objects", "--bucket", bucket_name,
    "--prefix", s3_folder_key, "--output", "json", "--no-sign-request"
]
objects_output = subprocess.check_output(list_objects_command, universal_newlines=True)
objects = json.loads(objects_output)["Contents"]

# Download each file from the S3 folder
for obj in objects:
    s3_key = obj["Key"]
    local_file_path = os.path.join(local_folder, s3_key)
    print(local_file_path)
    # Download the file
    download_command = ["aws", "s3", "cp", "s3://{}/{}".format(bucket_name, s3_key), local_file_path, "--no-sign-request"]
    try:
        subprocess.check_call(download_command)
        print("File downloaded successfully: {}".format(local_file_path))
    except subprocess.CalledProcessError:
        print("Error downloading file: {}".format(s3_key))

# Get all .gz files in the source folder
gz_files = [
    os.path.join(dirpath, filename)
    for dirpath, _, filenames in os.walk(local_folder)
    for filename in filenames
    if filename.endswith(".gz")
]
print(gz_files)
for file in gz_files:
    # Extract each .gz file
    print(file)
    # Open the .gz file and decompress it
    with gzip.open(file, 'rb') as f_in:
        # Get the output path without the .gz extension
        output_file = os.path.splitext(file)[0]
        # Open the output file in write mode
        with open(output_file, 'wb') as f_out:
            # Copy the contents of the .gz file to the output file
            f_out.write(f_in.read())
    print("File decompressed: {}".format(os.path.basename(file)))

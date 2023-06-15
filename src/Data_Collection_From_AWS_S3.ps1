
$bucketName = "genome-browser"
$s3FolderKey = "goldenPath/wuhCor1/bigZips"
$localFolder = "C:\genome-browser\"
$7zipPath = "C:\Program Files\7-Zip\7z.exe"

# Create the local folder if it doesn't exist
if (-not (Test-Path $localFolder)) {
    New-Item -ItemType Directory -Path $localFolder | Out-Null
}

# List the S3 objects in the folder
$objects = aws s3api list-objects --bucket $bucketName --prefix $s3FolderKey --output json --no-sign-request | ConvertFrom-Json

# Download each file in the S3 folder
foreach ($object in $objects.Contents) {
    $s3Key = $object.Key
    $localFilePath = Join-Path -Path $localFolder -ChildPath $s3Key
    echo $localFilePath
    # Download the file
    try {
        Write-Host "Downloading file: $s3Key"
        aws s3 cp s3://$bucketName/$s3Key $localFilePath --no-sign-request
        Write-Host "File downloaded successfully to: $localFilePath"
    } catch {
        Write-Host "Error downloading file: $s3Key"
    }
}

# Get all .gz files from the source folder
$gzFiles = Get-ChildItem -Path $localFolder -Filter "*.gz" -Recurse
echo $gzFiles
foreach ($file in $gzFiles) {
	# Extract each .gz file
	echo $file.FullName
    # To extract the .gz file
    & $7zipPath e $file.FullName -o$localFolder
    Write-Host "Unzipped file: $($file.Name)"
}

 
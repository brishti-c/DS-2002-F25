#!/usr/bin/env python3

import argparse
import requests
import boto3
import os

def download_file(file_url, local_filename):
    response = requests.get(file_url)
    response.raise_for_status()
    with open(local_filename, "wb") as f:
        f.write(response.content)
    return local_filename

def main():
    parser = argparse.ArgumentParser(description="Download a file, upload to S3, presign it.")
    parser.add_argument("--url", required=True, help="URL of the file to download")
    parser.add_argument("--bucket", required=True, help="S3 bucket name")
    parser.add_argument("--key", required=True, help="S3 object key")
    parser.add_argument("--expires", type=int, default=604800, help="Expiration time in seconds")

    args = parser.parse_args()

    local_file = args.key

    download_file(args.url, local_file)

    s3 = boto3.client("s3")
    s3.upload_file(local_file, args.bucket, args.key)

    presigned_url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": args.bucket, "Key": args.key},
        ExpiresIn=args.expires
    )

    print(presigned_url)

    if os.path.exists(local_file):
        os.remove(local_file)

if __name__ == "__main__":
    main()

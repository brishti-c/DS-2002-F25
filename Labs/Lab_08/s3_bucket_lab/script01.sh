#!/usr/bin/env bash
set -e

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local-file> <bucket-name> <expiration-seconds>"
    exit 1
fi

LOCAL_FILE="$1"
BUCKET="$2"
EXPIRATION="$3"

FILENAME=$(basename "$LOCAL_FILE")

aws s3 cp "$LOCAL_FILE" "s3://$BUCKET/$FILENAME"

aws s3 presign "s3://$BUCKET/$FILENAME" --expires-in "$EXPIRATION"


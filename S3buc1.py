import boto3

def create_s3_bucket(bucket_name, region="eu-central-1"):
    s3 = boto3.client("s3", region_name=region)

    # Create the bucket
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": region}
    )
    print(f"Bucket '{bucket_name}' created successfully.")

    # Enable versioning
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={"Status": "Enabled"}
    )
    print("Bucket versioning enabled.")

    # Public access settings are not blocked
    print("Public access settings are not blocked.")

# Usage
create_s3_bucket(
    bucket_name="my-open-bucket",
    region="eu-central-1"
)

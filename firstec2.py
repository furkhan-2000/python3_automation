import boto3

# Start a session with the specified AWS profile
session = boto3.Session(profile_name="AWS_FURRY")

# Create an EC2 resource
ec2 = session.resource('ec2')

# User data script
user_data_script = """#!/bin/bash
sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform

sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd

echo "hello, this is system-generated $(hostname -f)" > /var/www/html/index.html

sudo yum install -y docker
sudo systemctl start docker 
sudo systemctl enable docker 
"""

# Create an EC2 instance
try:
    instances = ec2.create_instances(
        ImageId='ami-08ec94f928cf25a9d',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='frankfurt_key',
        SecurityGroupIds=['sg-0fa7b4d7dbcc353b5'],
        SubnetId='071a02edd74e2ec6f',
        UserData=user_data_script
    )

    for instance in instances:
        print(f'Created EC2 instance with ID: {instance.id}')
except Exception as e:
    print(f"Error creating instance: {e}")

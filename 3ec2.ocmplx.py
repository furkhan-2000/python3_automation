import boto3

session = boto3.Session(profile_name="terra_user")

ec2 = session.resource('ec2')

user_data_script = """#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker

sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform

sudo yum install python3 -y
sudo yum install python3-pip -y
sudo pip3 install boto3

sudo yum install httpd -y
"""

try:
  
    instances = ec2.create_instances(
        ImageId='ami-xxxxxxx',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='canada_key',
        SecurityGroupIds=['sg-09a0f56566aa169d1'],  
        UserData=user_data_script,
        IamInstanceProfile={
            'Name': "custom-ssm"
        }
    )

    for instance in instances:
        print(f'This instance was created just now: {instance.id}')

except Exception as e:
    print(f"This is the error you were facing: {e}")

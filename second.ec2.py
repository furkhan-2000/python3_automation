import boto3

# Create a session with the specified profile
session = boto3.Session(profile_name="terra_user")

# Initialize the EC2 resource
ec2 = session.resource('ec2')

# User Data script to run on instance launch
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

sudo yum install -y java-17-amazon-corretto
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo tee /etc/yum.repos.d/jenkins.repo <<EOF
[jenkins]
name=Jenkins-stable
baseurl=https://pkg.jenkins.io/redhat-stable
gpgcheck=1
EOF
sudo yum update -y
sudo yum install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
"""

try: 
    # Create the EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0a90dcbc39d3ab358',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='lalu',
        SecurityGroupIds=['sg-0fa7b4d7dbcc353b5'],  # Changed SecurityGroupId to SecurityGroupIds
        SubnetId='0ff0ead645a7e56aa',
        UserData=user_data_script 
    )
    
    # Print the ID of the created instance
    for instance in instances:  # Changed `instance` to `instances`
        print(f'Created an instance with ID: {instance.id}')
except Exception as e: 
    print(f"Error creating instance: {e}")

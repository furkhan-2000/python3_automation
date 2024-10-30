import boto3

# Create a session using the specified profile
session = boto3.Session(profile_name='terra_user')

# Create an EC2 resource
ec2 = session.resource('ec2')

# User data script to run on instance launch
user_data_script = """#!/bin/bash 
sudo dnf update -y
sudo dnf install docker -y 
sudo systemctl start docker 
sudo systemctl enable docker

# Docker login command may need username and password, handle securely
# docker login 

sudo dnf install httpd -y 
sudo dnf install -y yum-utils shadow-utils
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo dnf -y install terraform

sudo dnf install python3 -y 
sudo dnf install python3-pip -y 
sudo pip3 install boto3

sudo dnf install tomcat -y 
sudo dnf install nginx -y 

sudo dnf install java-17-openjdk-devel -y
java -version
sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
sudo tee /etc/yum.repos.d/jenkins.repo <<EOF
[jenkins]
name=Jenkins
baseurl=https://pkg.jenkins.io/redhat-stable/
gpgcheck=1
gpgkey=https://pkg.jenkins.io/redhat/jenkins.io.key
EOF
sudo dnf install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins
sudo systemctl status jenkins
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
"""

try:
    # Create an EC2 instance
    instances = ec2.create_instances(  # Changed 'instance' to 'instances' to store multiple instances
        ImageId='ami-0a90dcbc39d3ab358',  # Make sure this AMI ID is valid in your region
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='lalu',
        SecurityGroupIds=['sg-0fa7b4d7dbcc353b5'],  
        UserData=user_data_script
    )

    for instance in instances:  # Iterate over 'instances' (the correct variable name)
        print(f'I created EC2 instance with ID: {instance.id}')  # Use 'instance' instead of 'inst'
        
except Exception as e:
    print(f'The error is: {e}')

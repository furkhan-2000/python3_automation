import boto3

session = boto3.Session(profile_name='terra_user')

ec2 = session.resource('ec2')

user_data_script = """
#!/bin/bash

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
"""

try:
   
    instances = ec2.create_instances(
        ImageId='ami-0f3a22468a3535271',  
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        SecurityGroupIds=['sg-0fa7b4d7dbcc353b5'],  
        UserData=user_data_script,
        IamInstanceProfile={
            'Name': "custom-ssm"  
        }
    )
    
    for instance in instances:
        print(f'This is the instance I created: {instance.id}')
except Exception as e:
    print(f"This is the error: {e} be careful!")

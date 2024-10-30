import boto3

# Create a session with the specified profile
session = boto3.Session(profile_name="terra_user")

# Initialize the EC2 resource
ec2 = session.resource("ec2")

# Specify the instance ID you want to delete
instance_id = "i-0c62954cfed110f68"

# Terminate the instance
instance = ec2.Instance(instance_id)
response = instance.terminate()

# Print the termination response
print(f"Termination response: {response}")

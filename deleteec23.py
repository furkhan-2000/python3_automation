import boto3

# Create a session using the specified profile
session = boto3.Session(profile_name='terra_user')  # Corrected syntax

# Create an EC2 resource
ec2 = session.resource("ec2")

# Define the instance ID (make sure to remove the comma)
instance_id = "i-0f1c7950cb699d5e0"  # Remove the comma

# Get the instance
instance = ec2.Instance(instance_id)

# Terminate the instance
response = instance.terminate()

# Print the response
print(f"This instance will get deprecated: {response}")

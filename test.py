import boto3

# Connect to EC2 client

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print("Instance Name: " + instance["InstanceId"])
        print("Public DNS: " + instance["PublicDnsName"])
        print("Zone: " + instance["Placement"]["AvailabilityZone"])

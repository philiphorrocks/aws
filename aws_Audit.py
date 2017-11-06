#!/usr/bin/env python
import boto3


def awsInstanceDetails():

    # Connect to EC2 client

    ec2client = boto3.client('ec2')
    response1 = ec2client.describe_instances()

    # Get list of all EC2 instances
    print("Getting list of EC2 instances:\n")

    for reservation in response1["Reservations"]:
        for instance in reservation["Instances"]:

            try:
                # This sample print will output entire Dictionary object
                #print(instance)
                id = instance["InstanceId"]
                print(id)
                # This will print will output the value of the Dictionary key 'InstanceId'
                print("Instance Name: " + instance["InstanceId"])
                print("Public DNS: " + instance["PublicDnsName"])
                print("Zone: " + instance["Placement"]["AvailabilityZone"])

                return instance["PublicDnsName"]

            except:

                print("Cannot get AWS instance details")


def awsGetVolumes():

    ec2 = boto3.resource('ec2')

    for i in ec2.instances.all():


        print("Id: " + i.id + "\nState: " + i.state['Name'])


def s3StorageDetails():

    # List all S3 stoage volumes available

    s3client = boto3.client('s3')

    s3Response = s3client.list_buckets()

    buckets = s3Response["Buckets"]

    # Test if there is value set for buckets.

    if buckets:

        print("buckets: " + str(buckets))

    else:

        print("No S3 Buckets configured")



# Main Method
if __name__ == '__main__':
    awsInstanceDetails()

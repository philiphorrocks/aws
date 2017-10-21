import boto3


def awsInstance():

    # Connect to EC2 client

    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances()

    # Get list of all EC2 instances
    print("Getting list of EC2 instances:\n")

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            try:
                # This sample print will output entire Dictionary object
                #print(instance)

                # This will print will output the value of the Dictionary key 'InstanceId'
                print("Instance Name: " + instance["InstanceId"])
                print("Public DNS: " + instance["PublicDnsName"])
                print("Zone: " + instance["Placement"]["AvailabilityZone"])

            except:

                print("Cannot get AWS instance details")


# Main Method
if __name__ == '__main__':

    awsInstance()

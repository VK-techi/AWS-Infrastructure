#List Instances(Image id, Instance id, Instance launch time) and Volume(State, Volumeid, Volume Type, Availability Zone) info
import boto3
from pprint import pprint #pprint --> print output in well structured manner in terminal
aws_man_con=boto3.session.Session(profile_name="default")
ec2_con_cli=aws_man_con.client(service_name="ec2",region_name="ap-south-1")

print("==================================================\n Instances")

response=ec2_con_cli.describe_instances()['Reservations']
for each_item in response:
    for each in each_item['Instances']:
        print("-----------------------------------------------")
        print(" Image id:{}\n Instance Id:{}\n Instance Launch Time: {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime']))

print("==================================================\n Volumes")  

vresponse=ec2_con_cli.describe_volumes()['Volumes']
for each_volume in vresponse:
    print("-----------------------------------------------")
    print(" State: {} \n Volume id: {} \n Volume Type: {} \n Availability Zone: {}".format(each_volume['State'],each_volume['VolumeId'],each_volume['VolumeType'],each_volume['AvailabilityZone']))

    for item in each_volume['Attachments']:
        print(" State: {}\n Delete on Termination: {}".format(item['State'],item['DeleteOnTermination']))






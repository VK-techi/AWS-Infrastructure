import boto3
aws_man_con=boto3.session.Session(profile_name="default")
iam_con=aws_man_con.client(service_name="iam")
s3_con=aws_man_con.client(service_name="s3")
ec2_con=aws_man_con.client(service_name="ec2")

#List all iam username
print("List of IAM UserName:\n")
response=iam_con.list_users()
for each in response['Users']:
    print(each['UserName'])

print("==========================================")

#List all S3 Buckets Name
print("\nList of S3 Bucket Names: \n")

sresponse=s3_con.list_buckets()
for each_bucket in sresponse['Buckets']:
    print(each_bucket['Name'])


print("==========================================")

#List all ec2 instanceId
print("\nList of EC2 Instances ImageId:\n")

eresponse=ec2_con.describe_instances()
for each in eresponse['Reservations']:
    for i in each['Instances']:
        print(i['InstanceId'])
    
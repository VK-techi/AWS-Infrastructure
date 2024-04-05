import boto3

aws_man_con=boto3.session.Session(profile_name="default")
iam_con=aws_man_con.resource("iam")
s3_con=aws_man_con.resource("s3")
ec2_con=aws_man_con.resource("ec2")

#List of all IAM UserName
print("List of IAM UserName:\n")
response=iam_con.users.all()

for each in response:
    print(each.user_name)

print("==========================================")


#List of all S3 buckets name
print("\nList of S3 Bucket Names: \n")
sresponse=s3_con.buckets.all()
for each_bucket in sresponse:
    print(each_bucket.name)

print("==========================================")

#List all ec2 instanceId
print("\nList of EC2 Instances ImageId:\n")

eresponse=ec2_con.instances.all()
for each_instance in eresponse:
    print(each_instance.instance_id)
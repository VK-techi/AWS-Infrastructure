import boto3
aws_man_con=boto3.session.Session(profile_name="default")
sts_con=aws_man_con.client("sts")  #Security Token Service

response=sts_con.get_caller_identity()
print(response['Account'])

"""
->STS enables us to create temporary, limited privileges credentials
to access AWS resources.
->Short-term credentials: we configure expiration period
"""
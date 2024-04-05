#program to print (username, user id and ARN) of all IAM users

import boto3
from pprint import pprint

aws_man_con=boto3.session.Session(profile_name="default")
iam_ser_con=aws_man_con.resource(service_name="iam")

#-------------------------details of individual user-------------------------------

#iam_user_obj=iam_ser_con.User('anup')   #Created a User resource  (created object)
#pprint(dir(iam_user_obj))               #print available properties or methods for created object (eg. user_id,user_name,policies)

#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User
#print("User Name: {} \t User Id: {} \t ARN {}".format(iam_user_obj.user_name,iam_user_obj.user_id,iam_user_obj.arn))


#------------------------details of all users-------------------------------------
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users
user_iterator=iam_ser_con.users.all() #Return type --> list(iam.User) 
for each_user in user_iterator:       #iterating throught list of iam.User
    print("User Name: {} \t User Id: {} \t ARN {}".format(each_user.user_name,each_user.user_id,each_user.arn))

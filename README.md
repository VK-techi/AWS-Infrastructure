# Boto3-Python-SDK


###########################################################################

-Boto3 is the name of the Python SDK for AWS.

-Boto3 allws us to directly create, update, and delete AWS services from our Python scripts.

-Boto3 is built on the top botocore module.

installing boto3(python version 3)
```pip3 install boto3```


--------------------
Configure AWS account credentials using aws cli
--------------------
---Install awscli
```pip3 install awscli```

---Configure root/IAM user:
```aws configure --profile <profile-name>```

provide access key and Secret access key
(Get it from IAM user-->Security Credentials)


Access key & Secret access keys are stored in .aws/credentials

#############################################################################

Steps to see/list iam users:
==================================

1. Get AWS management console
2. Get IAM console
    options: Users, Groups, role,..
    
====================================
```js
//create iam.py file  --> vi iam.py

import boto3
aws_man_con=boto3.session.Session(profile_name="default")  #getting aws management console
iam_con=aws_man_con.resource('iam') #getting service console ('s3'),('ec2'),('iam'),etc

for each_user in iam_con.users.all():    #options: users/groups/role
	print(each_user.name)                #printing all users

//run iam.py file --> python iam.py 

```

=================================

list all s3 buckets

=================================

```js

import boto3
aws_man_con=boto3.session.Session(profile_name="default")
s3_con=aws_man_con.resource('s3')

for each_bucket in s3_con.buckets.all():
	print(each_bucket.name)
	
```
=================================

Boto3 Concepts

-----------------------------------

The core conecepts of boto3:
    Session
    
    Resource
    
    Client
    
    Meta
    
    Collections
    
    Waiters
    
    Paginators

#Session:

	--> It is an AWS Management Console in our terms
	
	--> stores configuration information (primary credentials)
	
	--> allows us to create service clients and resources

Can create any no of sessions in one python boto3 script:

```js
import boto3
aws_man_con_root=boto3.session.Session(profile_name="root")
aws_man_con_dev=boto3.session.Session(profile_name="ec2_developer")

```

#Resource and Client

    --> We can create particular AWS Service Console like iam console, ec2 console, dynamodb console,...
    
    --> Resource is higher level object-oriented service access and it is available for some of the aws services(you can do . operations and not all operations of services are available)
    
    --> Client is low-level service access (in client output is dictonary in each and every step) all operations of service is available you can use either client or resources from your session object to create service console
    

```js
import boto3
aws_man_con=boto3.session.Session(profile_name="default")
iam_con_re=aws_man_con.resource(service_name="iam",region_name="ap-south-1")
iam_con_cli=aws_man_con.client(service_name="iam",region_name="ap-south-1")

```


 The dir() function returns all properties and methods of the specified object, without the values.

 Syntax: 
 
 ```dir(object)```

eg.
```js
 aws_man_con=boto3.session.Session(profile_name="default")
 dir(aws_man_con)

 print(aws_man_con.get_available_resouces())
```

 -----------------------------------------------

 ```js

 aws_man_con=boto3.session.Session(profile_name="default")
 iam_con_re=aws_man_con.resource("iam")
 iam_con_cli=aws_man_con.client("iam")

 #Listing iam users with resource object:

 for each_user in iam_con_re.users.all():
    print(each_user.name)

#Listing iam users with client object:

for each in iam_con_cli.list_users()['Users']:
    print(each['UserName'])

"""
>>iam_con_cli=aws_man_con.client("iam")
>>print(iam_con_cli)
>>print(iam_con_cli.list_users()) #gives output as a dictionary
>>print(iam_con_cli.list_users()['Users']) #Key->['Users']--> gives *list* of users
as we get *list* we take for loop
>>for each in iam_con_cli.list_users()['Users']:
    print(each)
>>for each in iam_con_cli.list_users()['Users']:
    print(each['UserName'])
"""

 ```



_____________________________________________________

Boto3 Session Concept:
There are 2 Types of Sessions:

    1. Custom Session
    
        aws_man_con=boto3.session.Session(profile_name="default")
        iam_con_re=aws_man_con.resource("iam")

    2. Default Session(official documentation completely based on default session)
    
    https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
        iam_con_re=boto3.resource("iam")

___________________________________________________________________

Dealing with client

```js
import boto3
aws_man_con=boto3.session.Session(profile_name="default")
iam_con=aws_man_con.client(service_name="iam")

response=iam_con.list_users()
print(response)

```


-----------------------------------------------------------
list all ec2  instance IDs
___________________________________________________________

```js
import boto3
aws_man_con=boto3.session.Session(profile_name="default")
ec2_con=aws_man_con.client("ec2")

response=ec2_con.describe_instances()

for each in response['Reservations']:
    for i in each['Instances']:
        print(i['ImageId'],i['Monitoring'])
    print('======================')
    
```

------------------------------------------------------------
list all s3 buckets Name
____________________________________________________________

```js
import boto3
aws_man_con=boto3.session.Session(profile_name="default")
s3_con=aws_man_con.client("s3")

response=s3_con.list_buckets()

for each_bucket in response['Buckets']:
    print(each_bucket["Name"])
    print("==========================")

```



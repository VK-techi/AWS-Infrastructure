#Menudriven python program to perform actions on ec2 instance using resource

import boto3
import sys
from pprint import pprint #to print available properties/actions of an object in structured manner
aws_man_con=boto3.session.Session(profile_name="default") # access management console 
ec2_con_re=aws_man_con.resource('ec2')                    # access service

while True:
    print("""
    Script performs following actions on EC2 Instance

    1.Start
    2.Stop
    3.Terminate
    4.Exit""")

    option=int(input("Please select option:"))

    if(option==1):
        i_id=input("Please enter instance id: ")
        my_instance_obj=ec2_con_re.Instance(i_id) #my_instance_obj object created
        #pprint(dir(my_instance_obj))             #list all properties and methods available for given object
        my_instance_obj.start()             
        print("EC2 instance Starting....")
    
    elif(option==2):
        i_id=input("Please Enter Instance Id: ")
        my_instance_obj=ec2_con_re.Instance(i_id)
        my_instance_obj.stop()    
        print("EC2 instance Stopping....")
    
    elif(option==3):
        i_id=input("Please Enter Instance Id: ")
        my_instance_obj=ec2_con_re.Instance(i_id)
        my_instance_obj.terminate()    
        print("EC2 Instance Terminating....")

    elif(option==4):
        print("Thanks you for using this script")
        sys.exit()
    
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nPlease select Valid Option\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
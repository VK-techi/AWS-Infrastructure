from email.message import Message
from socket import timeout
from urllib import response
import boto3
from pprint import pprint

aws_man_cons=boto3.session.Session(profile_name='default') #get access of aws management console access
sqs=aws_man_cons.client('sqs') #get service access

#pprint(dir(service_access))  #list of operations available for created object 
# output send_message  receive_message

#output is list ... need to perfrom . operations



#created function to create queue

def createqueue():
    queuename=input("Enter the Queue name:")
    queue = sqs.create_queue(
        QueueName=queuename,
         Attributes={
             'DelaySeconds': '5'  #Delay queues make messages unavailable to consumers for a specific period of time. 
                                  #a message is hidden when it is first added to queue
             }
         )

#------------------------------------------Queue is created---------------------------------------------------------# 

# URL of queue 
  
    response=sqs.get_queue_url(
            QueueName=queuename
            )
    print(response)

#____________________________________________________________________________________________________________________

#function to send message to queue

def sendmsg():
    queueurl=input("Enter the Queue URL form above:")
    msg=input("Enter the msg you want to send:")  #taking input from user to sent message

    response=sqs.send_message(
        QueueUrl=queueurl,
        MessageBody=(
            msg
        )
     #dir(response)  check parameters required from dir(response) error or doc
    )
    print(response['MessageId'])

#------------------------------------------Message sent to queue------------------------------------------------------

# function to receive message

def receivemsg():
    queueurl=input("Enter the Queue URL form above:")
    response = sqs.receive_message(
        QueueUrl=queueurl
    )
    message = response['Messages'][0]
    

    pprint(f"Number of messages received: {len(response.get('Messages', []))}") #printing the length of messages
    pprint('Received  message: %s' % message) # message body


    #delete message
    for msg in response['Messages']:
        msg_body = msg['Body']
        receipt_handle = msg['ReceiptHandle']
        response = sqs.delete_message(
            QueueUrl=queueurl,
            ReceiptHandle=receipt_handle,
        )
    print(response)

#---------------------------------------Message received and Deleted from queue---------------------------------

# function to delete queue

def deletequeue():
    queueurl=input("Enter the Queue URL form above:")

    sqs.delete_queue(QueueUrl=queueurl)
    

#---------------------------------------queue deleted-----------------------------------------------------------

while True:
    print("\nSQS menu")
    print("\n1. Create SQS Queue")
    print("\n2.Send message to Queue")
    print("\n3.Recieve and delete message from Queue")
    print("\n4. Delete Queue")
    print("\n5.Exit")
    choice=int(input("\nEnter your choice:"))

    if choice==1:
        createqueue()  # function call

    elif choice==2:
        sendmsg()

    elif choice==3:
        receivemsg()
    
    elif choice==4:
        deletequeue()

    elif choice==5:
        break

    else:
        print('Provide a valid input')




# Visibility Timeout:
#To prevent other consumers from processing the message again, 
#Amazon SQS sets a visibility timeout, a period of time during 
#which Amazon SQS prevents other consumers from receiving and 
#processing the message. The default visibility timeout for a message is 30 seconds.

#Three condition of visibility timeout
#1) message is processed withing visibility timeout --> API is called and message will be deleted from queue
#2) consumers require extra time to process message  --> API called and visibility timeout increases
#3) consumers failed to process within visibility timeout --> If a consumer fails to process a message within the 
#Visibility Timeout… the message goes back to the queue!
#• We can set a threshold of how many times a message can go back to the queue 
#• After the MaximumReceives threshold is exceeded, the message goes into a dead letter queue (DLQ) will be checked by operation team manually.

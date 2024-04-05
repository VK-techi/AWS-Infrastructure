import boto3

aws_man_con=boto3.session.Session(profile_name='default') #management console access

# Create SQS client
sqs=aws_man_con.client('sqs')


queue_url = 'https://sqs.us-west-2.amazonaws.com/022536741821/q' #create queue in management console & paste url here

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Message sent from queue'
        'successfully.'
    )
)

print(response['MessageId'])

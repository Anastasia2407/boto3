import boto3

print("""AWS Menu:
1. Deploy EC2
2. Delite EC2
3. Describe instances
4. Stop EC2
5. Start EC2""")
ec2 = boto3.resource('ec2')
boolean = 0
while boolean == 0:
    answer = input("Your choise is: ")
    if answer == 1:
        instances = ec2.create_instances(
            ImageId='ami-0d5d9d301c853a04a',
            MinCount=1,
            MaxCount=2,
            InstanceType='t2.micro',
            KeyName='Devops'
        )
        boolean = 1
    elif answer == 2:
        newlist = []
        ids = raw_input("what is ID of your instance")
        ec2.instances.filter(InstanceIds=newlist).terminate()
    elif answer == 3:
        for instance in ec2.instances.all():
            print("Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState {5}\n".format(
                instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id,
                instance.state
            )
            )
            boolean = 0
    elif answer == 4:
        newlist = []
        ids = raw_input("what is ID of your instance")
        ec2.instances.filter(InstanceIds=newlist).stop()
        boolean = 0
    elif answer == 5:
        newlist = []
        ids = raw_input("what is ID of your instance")
        ec2.instances.filter(InstanceIds=newlist).start()
        boolean = 0
    else:
        print("Choose from 1 to 5!!!")

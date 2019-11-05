import boto3

ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
     ImageId='ami-0d5d9d301c853a04a',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='Devops'
)

instances = ec2.create_instances(
     ImageId='ami-055e9447843bc8f47',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='Devops'
 )

for instance in ec2.instances.all():
    print(
        "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState {5}\n".format(
        instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
        )
    )

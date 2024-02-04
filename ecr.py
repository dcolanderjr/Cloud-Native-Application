# Use python to create your ECR Repo, this was performed using Terraform. Alternatively, you can do it manually through the console.

import boto3

ecr_client = boto3.client("ecr")

repository_name = "my-cloud-native-repo"
response = ecr_client.create_repository(repositoryName=repository_name)


repository_uri = response["repository"]["repositoryUri"]
print(repository_uri)

# Store tfstate file in S3 BUcket

terraform {
    backend "s3" {
        key = "eks/terraform.tfstate"
        bucket = "tf-state-backup-dc"
        region = "us-east-1"
        access_key = ""
        secret_key = ""
    }
}
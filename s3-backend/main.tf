# Simple S3 bucket creation, with versioning enabled
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "TFState-File" {
    bucket = "tf-state-backup-dc"

        tags = {
        Name        = "TF-State_Bucket-DC"
        Environment = "prod"
  }
}

resource "aws_s3_bucket_versioning" "TFState-File-Versioning" {
  bucket = "tf-state-backup-dc"
  versioning_configuration {
    status = "Enabled"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.TFState-File.id
}
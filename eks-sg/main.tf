# Code creates a generic security group with port 5000 open so it can be used on local machine, as well as accessed from internet.

provider "aws" {
  region = "us-east-1"
}


resource "aws_security_group" "eks-sg" {
    name = "eks-sg"
    description = "Allow EKS Local"
    ingress {
        from_port = 5000
        to_port = 5000
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
   }
}   

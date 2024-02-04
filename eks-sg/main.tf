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
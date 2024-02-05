This is a cloud native application that is written in python/flask that monitors CPU usage. The application starts off as a docker file, and then we move it to Kubernetes hosted on AWS.

Prerequisites

1: You need to create an AWS account, all of this should be in the free tier. You need to have programmatic access to the console, so if you do not currently have access keys, you need to go into the IAM console, request access keys for your user, and then configure them in the CLI. To download the CLI, perform a quick search for "AWS CLI" to get started. WARNING: If this is your first time creating access keys, you will need to ensure that when you create them, you save the .csv file to your local machine; once you click out of the screen where it shows your secret key, you can never view it in the console again. If you skip this step, you will have to create new keys. Once you have your keys, open up the cmd prompt, and type aws configure. It will first ask you for your access key, the secret key, then region (the region you will deploy the project from) and an output format, use json. Once you have completed this step, continue.

2: Determine if you have python3 installed on your local machine by using the cmd line, type in python --version, if you do not, pip install python3.

3: Docker and Kubectl, you need to ensure you have both of these applications to install as we will be using docker to create the image, verify your setup with docker --version, kubectl version, pip install python, pip install kubectl.

4: You need a code editor, use VS Code if you do not have one.  Once you get all of the prerequisites done, lets move on. This is a microsoft product, it is on their site.

Here we go:

#Instructions will be for VSCode, but your code editor should be set up just fine:

Create a folder, name it cloud-native-application
The first module you should access from the repository is the app.py file, this file contains the instructions to import the psutil and Flask. Very important, use the pip3 install flask, and pip3 install psutil. You will need these two to run the application. They can be downloaded right in the terminal on VSCode. 

The next module you will need to access is the requirements.txt, run pip3 install -r requirements.txt, it will go ahead and start installing all the additional dependent modules. After you perform the downloads, type in "python3 app.py"

The app.py file should be running now. In the terminal window it will have the port that it is running on, it should be port 5000. Verify the application is running by returning to your web browser, type localhost:5000 in the search bar. Pay attention to the terminal by making your window small, you should get 200 messages, meaning the application is working. This is not the finished product, we still have more work to do. Back to VSCode. Type ctrl+c to stop the application.

![app py](https://github.com/dcolanderjr/Cloud-Native-Application/assets/131455625/7bc9a793-a442-42a6-a4ad-065ab152db48)

The next items you should reference are in the templates folder. Create a folder named templates, and include the HTML file in the folder. The HTML does all the leg work to make our application a little bit more appealing. (Long story short, our text app was kind of bland, so now its a new app, with fancy gauges!) Restart the application in the terminal by running "python3 app.py", you should now see the gauges.

Next, we will create the docker file that will be used to host this in a container. The file contents contain (see what I did there) all the dependencies needed to run the application. Similar to what we did with the requirements.txt file and imported into the app.py file, we will import this into the docker container. Good thing about containers is they can run all of the dependencies within itself instead of having to rely on apps on the underlying hardware. Just a quick run down of what the docker file does: Declares the python runtime, creates a folder for the application to run in, and pulls in the dependencies from the requirements.txt file. Sets the environment variables, installs any python updates, and exposes the localhost:5000 port. The dependencies download also installs boto3 (aws python) as well as Kubernetes. To get the container to run, use the command "docker build -t my-flask-app ." (ensure the space after the flask app) Afterwards, run "docker images" to verify your image completed. Next, run "docker run - p" to determine the port and IMAGEID (should be 5000). Next run the command, "docker run -p 5000:5000 IMAGEID" (insert your image ID) Your docker container should be running, verify again by going to localhost:5000 in your browser, congrats its on Docker now!

![docker](https://github.com/dcolanderjr/Cloud-Native-Application/assets/131455625/c74c6d04-31d2-4b4e-ae9e-95c874a93392)

Now, we need to push our application to ECR. I used ECR because we are going to deploy the Kubernetes cluster on EKS. In the management console on AWS, search for ECR, and navigate to the ECR landing page. You have two options in creating your ECR repository, either use the "ecr.py" file and "python 3 ecr.py", or manually create it in the console. Either way, make sure you use the name provided in the file as the repository name to keep things consistent. When your repo is done creating, take note of the accountid.dkr.ecr.your-region.amazon.aws.com (replace accountID with your accountID, and your-region with the region you are working out of)

![ecr](https://github.com/dcolanderjr/Cloud-Native-Application/assets/131455625/782f10c4-8717-4cbb-8fa9-4c7082f8baac)

Verify your repository is created by returning to ECR in the management console. Click on your repo, and click the "View push commands" button. This will bring up a popup window with commands you need to run in order. Run the the four commands back in the terminal in VSCode. The first will retrieve an STS token which will provide the temporary credentials for you to push your repo to ECR, the second command will build the docker image, the third command will tag your immage, and the final command will push the image to the repository.

![ecr-instructions](https://github.com/dcolanderjr/Cloud-Native-Application/assets/131455625/ba38b773-6fb3-401d-b6ed-eaca1b1223ca)

Now, while still in the management console, move over to the IAM page. Click on roles on the left hand side, and create a new role. Name the role 'EKSNodeRole' or something of the sort, and and attach the following policies to it:   AmazonEKS_CNI_Policy, AmazonEKSClusterPolicy, AmazonEKSServicePolicy. Review the policy, and create the role. 

WARNING: I struggled with this part of the project, everytime I deployed my cluster it would come back unhealthy, and I could not launch any nodes on my cluster, but eventually I found it out. What's a little fun amongst friends? I am intentionally leaving a step of this hidden, so you can explore documentation and get the answers in the event your cluster will not deploy properly. You will be frustrated, but do not give up. I have included a JSON file with the correct policy as well if you wish to complete the rest of this step via the CLI; however, I do encourage you to troubleshoot, its part of tech! Read between the lines here, and your answer is right in front of you. =D

Before you deploy your cluster, you need a security group that allows access for port 5000 to be open. In the eks-sg group, there are two files, a backend.tf and a main.tf, open the main.tf file. This file has the configuration you will need to attach to your EKS cluster when launching, so this step needs to be performed first. If you do not have terraform installed in VS Code, do the following: on the left hand tool bar there should be an icon with squares, one being detached, click on it, and type in "terraform" in the bar. Download and install the terraform plugin, you may be prompted to restart the editor. Once back up, access the file again and run the following commands, in order: 'terraform init' once that completes, run 'terraform plan', finally run 'terraform apply'. This should deploy your security group on AWS, go in and verify that you have the security group by typing in EC2 in the console, and on the left hand side scroll down and click on security groups.


![image](https://github.com/dcolanderjr/Cloud-Native-Application/assets/131455625/7db446c6-329d-4e36-be57-58140ae9720b)

Now, move over to the EKS console, and create the cluster. Name it 'cloud-native-cluster', leave the default for Kubernetes version, choose the role you created earlier under "Cluster Service Role" this next part is really important, do not change anything else on the screen, click next. Below is a screenshot of how I set mine up, your cluster needs to be in a public subnet with internet access, so just use the default VPC with the public subnets. Under security group, choose the group we created. On the next page, scroll down and click next, no monitoring on this one. On the add-ons page, leave the defaults, click next. On the configure add-ons page, leave the defaults, click next. Review, and click create. The cluster will take some time to come up, so I have provided a side quest in the meantime.

![image](https://github.com/dcolanderjr/Cloud-Native-Application/assets/131455625/b586b6f7-a8ed-4f34-9241-c07ebbc69e14)

SIDE QUEST: It's best practice to store your tfstate files somewhere else where they can be accessed in the event you delete it, or in a production environment with multiple people working on it at a time, can access it. Within the eks-sg folder, and the s3-backend folder, there are two tf files: one called main.tf, and backend.tf respectively in both folders. Open the s3-backend folder, and view the main.tf file. This file creates a simple bucket, with versioning enabled.




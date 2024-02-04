This is a cloud native application that is written in python/flask that monitors CPU usage. The application starts off as a docker file, and then we move it to Kubernetes hosted on AWS.

Prerequisites

1: You need to create an AWS account, all of this should be in the free tier. You need to have programmatic access to the console, so if you do not currently have access keys, you need to go into the IAM console, request access keys for your user, and then configure them in the CLI. To download the CLI, perform a quick search for "AWS CLI" to get started.

2: Determine if you have python3 installed on your local machine by using the cmd line, type in python --version

3: Docker and Kubectl, you need to ensure you have both of these applications to install as we will be using docker to create the image, verify your setup with docker --version, kubectl version. 

4: You need a code editor, use VS Code if you do not have one.  Once you get all of the prerequisites done, lets move on.

Here we go:

#Instructions will be for VSCode, but your code editor should be set up just fine:

Create a folder, name it cloud-native-application
The first module you should access from the repository is the app.py file, this file contains the instructions to import the psutil and Flask. Very important, use the pip3 install flask, and pip3 install psutil. You will need these two to run the application. They can be downloaded right in the terminal on VSCode. 

The next module you will need to access is the requirements.txt, run pip3 install -r requirements.txt, it will go ahead and start installing all the additional dependent modules. After you perform the downloads, type in "python3 app.py"

The app.py file should be running now. In the terminal window it will have the port that it is running on, it should be port 5000. Verify the application is running by returning to your web browser, type localhost:5000 in the search bar. Pay attention to the terminal by making your window small, you should get 200 messages, meaning the application is working. This is not the finished product, we still have more work to do. Back to VSCode. Type ctrl+c to stop the application.

![app py](https://github.com/dcolanderjr/Cloud-Native-Application/assets/131455625/7bc9a793-a442-42a6-a4ad-065ab152db48)

The next items you should reference are in the templates folder. Create a folder named templates, and include the HTML file in the folder. The HTML does all the leg work to make our application a little bit more appealing. (Long story short, our text app was kind of bland, so now its a new app, with fancy gauges!) Restart the application in the terminal by running "python3 app.py", you should now see the gauges.

Next, we will create the docker file that will be used to host this in a container. The file contents contain (see what I did there) all the dependencies needed to run the application. Similar to what we did with the requirements.txt file and imported into the app.py file, we will import this into the docker container. Good thing about containers if they can run all of the dependencies within itself instead of having to run on the underlying hardware.

![docker](https://github.com/dcolanderjr/Cloud-Native-Application/assets/131455625/c74c6d04-31d2-4b4e-ae9e-95c874a93392)




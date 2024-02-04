# Below is the code to create the python/flask app. Use pip install psutil if you do not have it currently on your system.

# import psutility, Flask
import psutil
from flask import Flask, render_template

#Variable for Flask 
app = Flask(__name__)

# Where app is deployed, cpu_percent/mem_percent where metrics in dashboard are pulled from.
# Return render_template references the index.html file for web interface of app
@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU Usage or High Memory Usage Detected. Please Scale Accordingly."
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)

# debug / app updates to terminal, review http:/1.1 200 message in terminal on app refresh in browser
# use IP address of localhost:5000 to access on local machine
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

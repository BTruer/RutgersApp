import requests
import json
import time
import atexit
from flask import Flask, render_template, request
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

app = Flask(__name__)

def fetch_from_api():
	f = open('food.txt','w')
	f.write(requests.get("https://rumobile.rutgers.edu/1/rutgers-dining.txt").content)
	f.close()

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=fetch_from_api,
    trigger=IntervalTrigger(seconds=3600),
    id='calling_api',
    name='call the api and update the data every hour',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

@app.route("/", methods=['GET'])
def index():
		f = open('food.txt','r')
		data = json.loads(f.read())
		bc_data = data[0]
		bdh_data = data[1]
		ldc_data = data[2]
		ndh_data = data[3]		
		f.close()
		return render_template('index.html', bc_data=bc_data, bdh_data=bdh_data, ldc_data=ldc_data, ndh_data=ndh_data)


@app.route("/update")
def getTest():
	f = open('food.txt','w')
	f.write(requests.get("https://rumobile.rutgers.edu/1/rutgers-dining.txt").content)
	f.close()
	return "tty"

if __name__ == '__main__':
    app.run(debug=True)




#### to do   make the update cron jon and make the rest of the dhalls like brower
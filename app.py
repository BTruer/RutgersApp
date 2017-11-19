import requests
import json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	if request.method == 'GET':
		f = open('food1.txt','r')
		data = json.loads(f.read())
		bc_data = data[0]
		bdh_data = data[1]
		ldc_data = data[2]
		ndh_data = data[3]		
		return render_template('index.html', bc_data=bc_data, bdh_data=bdh_data, ldc_data=ldc_data, ndh_data=ndh_data)


@app.route("/update")
def getTest():
	f = open('food.txt','w')
	f.write(requests.get("https://rumobile.rutgers.edu/1/rutgers-dining.txt").content)
	f.close()
	return "tty"

if __name__ == '__main__':
    app.run(debug=True)
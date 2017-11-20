# RutgersApp
Tells you what the vegetarian or vegan options are at the dining halls because before it was unclear.
It should include some amount of crowd sourcing although right now it does not.
The application will pull from the api once an hour an update the data which is stored locally as text. This avoid unnessary calls. Next the data is pushed into a html template. This design minimizes loading times and does not really on network and lets the data processing happen on the client.

how to run:
1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r req.txt`
4. `FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run`



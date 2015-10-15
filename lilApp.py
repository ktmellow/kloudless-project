#! python2.7
# Include API_KEY as argument

from flask import Flask, flash, redirect, render_template, request, session, abort, make_response
import urllib
import requests
import json
from sys import argv

# import pdb; pdb.set_trace()

API_KEY = argv[1]
APP_ID = 'Y9zKGOVamfBLiBhCPvoFRKMupn3H5Trxh_4ThDd__OG4Zy7g'

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("myTemplate.html")
	
@app.route('/', methods=['POST'])
def my_form_post():
    service = request.form['text2'] 
    search = request.form['text3']
    query_params = {
    	'callback': "http://localhost:5000/next/callback/?search=%s" % search,
    	'app_id': APP_ID
    }
    redirect_url = "https://api.kloudless.com/services/%s?%s" % (service, urllib.urlencode(query_params))
    return redirect(redirect_url, 302)

@app.route("/next/callback/")	
def next():
    search = request.args['search']
    service = request.args['service']
    account = request.args['account']
    search_link = "https://api.kloudless.com:443/v0/accounts/"+account+"/search/?q="+search
    headers = {
        'Authorization': 'ApiKey ' + API_KEY
    }
    search_results = requests.get(search_link, headers=headers)
    results_objects = json.loads(search_results.text)
    return render_template("nextTemplate.html", search=search, service=service,
                           account=account, results_objects=results_objects)

@app.route("/results/") 
def results():

    account = request.args['account']
    search = request.args['search']
    file_id = request.args['file_id'] 
    headers = {
        'Authorization': 'ApiKey ' + API_KEY,
        'Content-Type': 'application/json'
    }
    data = {'file_id': file_id}
    make_link = requests.post("https://api.kloudless.com/v0/accounts/"+account+"/links", 
                              headers=headers, data=json.dumps(data))

    return redirect(make_link.json()['url'])

if __name__ == "__main__":
	app.run(debug=True)
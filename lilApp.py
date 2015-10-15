from flask import Flask, flash, redirect, render_template, request, session, abort, make_response
import urllib
import requests
from requests.auth import HTTPBasicAuth
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
    #resp = make_response(redirect("https://api.kloudless.com/services/?app_id=Y9zKGOVamfBLiBhCPvoFRKMupn3H5Trxh_4ThDd__OG4Zy7g&callback=http%3A%2F%2Flocalhost%3A5000%2Fnext%2Fcallback"+"%3F"+search+"%3D"+search+"%26services%3D"+service, 302))
    #resp.set_cookie('search', 'search')
    #return resp
    return redirect(redirect_url, 302)

@app.route("/next/callback/")	
def next():
	#search=request.cookies.get('search')
	#service=request.cookies.get('service')
    search = request.args['search']
    service = request.args['service']
    account = request.args['account']

    search_link = "https://api.kloudless.com:443/v0/accounts/"+account+"/search/?q="+search
    search_results = requests.get(search_link, auth=HTTPBasicAuth(APP_ID, API_KEY))
   
    results_objects = json.loads(search_results.text)
    return render_template("nextTemplate.html", search=search, service=service,
                           account=account, results_objects=results_objects)

@app.route("/results/") # should be a GET request
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
    #return render_template("resultsTemplate.html", search=search, make_link=make_link, test=test)

if __name__ == "__main__":
	app.run(debug=True)







# note to self: fix style before asking for help
# refresher: (list, [array, {dictionary
# jinja only accepts dictionary values as dictionary.key --> value; NOT dictionary[key]

# want to learn: set/get cookies, pdb, VIM.
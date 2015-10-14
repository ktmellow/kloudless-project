from flask import Flask, flash, redirect, render_template, request, session, abort, make_response
import urllib
import requests
from requests.auth import HTTPBasicAuth
import json
from sys import argv

sys, API_KEY = argv
APP_ID = 'Y9zKGOVamfBLiBhCPvoFRKMupn3H5Trxh_4ThDd__OG4Zy7g'

app = Flask(__name__)

@app.route("/")
def index():
	#Kloudless.authenticator(element, params, callback);
    # api search 
	# return a link or something 	
	return render_template("myTemplate.html")
	
@app.route('/', methods=['POST'])
def my_form_post():
    service = request.form['text2'] 
    search = request.form['text3']
    query_params = {
    	'callback': "http://localhost:5000/next/callback/?search=%s" % search,
    	'app_id': APP_ID
    }
    #redirect_url = "https://api.kloudless.com/services/%s?%s" % (service, urllib.urlencode(query_params))
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
    all_id = []
    # print results_text 
    # lots of junk, must further filter it 
    for every_object in range(len(results_objects['objects'])-1):
        # for every object in page_json, get ID 
        all_id[every_object] = results_objects['objects'][every_object][2][id]
        print all_id
# YOU don't need a loop, just send a loop to template with curly braces


    # make a link (post) for each file or folder, works for files/folders POST /accounts/{account_id}/links/ only need account and file id
    # use requests instead of curl to handle this^ (see make a link doc in docs)
    return render_template("nextTemplate.html", search=search, service=service, account=account)


if __name__ == "__main__":
	app.run(debug=True)
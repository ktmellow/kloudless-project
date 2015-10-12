from flask import Flask, flash, redirect, render_template, request, session, abort, make_response
import urllib

app = Flask(__name__)

APP_ID = 'Y9zKGOVamfBLiBhCPvoFRKMupn3H5Trxh_4ThDd__OG4Zy7g'

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
	return render_template("nextTemplate.html", search=search, service=service)
# use account id from callback URL	
# https://api.kloudless.com:443/v0/accounts/86879941/search/?q=Pics
# need to authorize first with API Key!
	
if __name__ == "__main__":
	app.run(debug=True)
#note to self: hardcode the app id, but not the key 

from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    # authenticate with js stuff, also ask for storage and app id 
	#Kloudless.authenticator(element, params, callback);
	# find how to submit search word(s)
    # api search 
	# return a link or something 	
	return render_template("myTemplate.html")
	
@app.route('/', methods=['POST'])
def my_form_post():
    service = request.form['text2'] 
    #return redirect("https://api.kloudless.com/services/?app_id=Y9zKGOVamfBLiBhCPvoFRKMupn3H5Trxh_4ThDd__OG4Zy7g&callback=http%3A%2F%2Flocalhost%3A5000%2Fnext%2Fcallback&search="+search+"&services="+service, 302)
    #return redirect("https://api.kloudless.com/services/?app_id=Y9zKGOVamfBLiBhCPvoFRKMupn3H5Trxh_4ThDd__OG4Zy7g&callback=http%3A%2F%2Flocalhost%3A5000%2Fnext%2Fcallback%2F"+"&search="+search+"&services="+service, 302)
	#ampersand search term as url query to remember it
    return redirect("https://api.kloudless.com/services/?app_id=Y9zKGOVamfBLiBhCPvoFRKMupn3H5Trxh_4ThDd__OG4Zy7g&callback=http%3A%2F%2Flocalhost%3A5000%2Fnext%2Fcallback&services="+service, 302)


@app.route("/next/callback/")	
def next():
    return render_template("nextTemplate.html")

@app.route("/next/callback/", methods=['POST'])
def next_form():
# use account id from callback URL	
# https://api.kloudless.com:443/v0/accounts/86879941/search/?q=Pics
# need to authorize first with API Key!
# how to prevent losing URL parameters??  
    search = request.form['text3'] 
    return "Your \'" + search + "\' is located here: <link>"	
	
	
	
if __name__ == "__main__":
	app.run(debug=True)


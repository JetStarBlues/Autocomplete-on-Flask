import os
import re
from flask import Flask
from flask import render_template, request, Response, url_for

app = Flask(__name__)


# Home page
@app.route('/')
@app.route('/index.html')
def landingPage():
	return render_template('index.html')


# Thanks page
@app.route('/thanks.html')
def thanksPage():
	return render_template('thanks.html')


# Autocomplete script
@app.route('/auto_python.cgi', methods=['GET', 'POST'])
def findUsers():
	if request.method == 'GET':
		print("why heloo there")

		# Get the query
		q = str( request.args.get("to") )	# http://stackoverflow.com/q/11774265

		# We will store our response HTML here
		html = ''

		# Our limited 'database' contains a few users
		# with their username and full name
		data = [
			{
				"user" : "amon",
				"name" : "N. Equalist"
			},
			{
				"user" : "android18",
				"name" : "Bad Ass"
			},
			{
				"user" : "ayeka",
				"name" : "Crown Princess of the Imperial Family of Jurai"
			},
			{
				"user" : "gaara",
				"name" : "Sandy"
			},
			{
				"user" : "goku",
				"name" : "Kakarot"
			},
			{
				"user" : "hiruma",
				"name" : "Yoichi Hiruma"
			},
			{
				"user" : "naruto",
				"name" : "The next Hokage"
			},
			{
				"user" : "rockLee",
				"name" : "Rock Lee"
			},
			{
				"user" : "ryoko",
				"name" : "Space Pirate Ryoko"
			},
			{
				"user" : "sakura",
				"name" : "S&S Forever"
			},
			{
				"user" : "sasuke",
				"name" : "Sasuke Uchiha"
			},
			{
				"user" : "vegeta",
				"name" : "Saiyan Prince"
			}
		]

		# We "search" through the data
		regex = re.escape( q )

		for row in data:
			# Looking for users that match our auto-complete search
				# stackoverflow.com/a/14225664/2354735
				# stackoverflow.com/a/500870/2354735
			if ( re.search(regex, row["user"], re.IGNORECASE) is not None or 
			     re.search(regex, row["name"], re.IGNORECASE) is not None ):  
				
				html += ('<li id="' + row["user"] + '">' +
						 '<img class="icon" src="' + url_for('static') + 'icons/' + row["user"] + '.png"/>' +
						 '<div id="uDetails">' +
						 '<span id="username">' + row["user"] + '</span>' +
						 '<span> : </span>' +
				    	 '<span id="fullname">' + row["name"] + '</span>' +
				    	 '</div></li>')
		
		# And send the "response"
		return Response(html, mimetype='text/html') 	# http://stackoverflow.com/a/11774026



# Start Server
if __name__ == '__main__':
	# app.run()
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
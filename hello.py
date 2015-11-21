import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def landingPage():
	return render_template('index.html')


@app.route('/auto_python.cgi', methods=['GET', 'POST'])
def findUsers():
	if request.method == 'GET':
		print("why heloo there")
		query = request.args.get("to")
		print("keyword received was ", query)
		print( query )
		print( type(query) )
		print("qstring was ", request.query_string)


@app.route('/thanks.html')
def thanksPage():
	return render_template('thanks.html')



# Start Server
if __name__ == '__main__':
	# app.run()
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
import os
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')

def landingPage():
	print("tlandingPage() called")
	render_template('index.html')


# @app.route('/auto_python', methods=['GET', 'POST'])

# def findUsers():
# 	if request.method == 'GET':
# 		do_the_thing()



# Start Server
if __name__ == '__main__':
	# app.run()
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
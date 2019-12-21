__author__ = "Joshua Akangah"

from flask import Flask, render_template, url_for, request, redirect
from loc import *
import json

data = None

app = Flask(__name__)

def flatten_data(dat):
	flat = []
	for i in search(dat):
		flat.append([i[0]['lat'], i[1]['lon']])
	return flat

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		file = request.files['filename']
		global data
		data = json.loads(file.read())
		return redirect('/map')
	return render_template('index.html')

@app.route('/map')
def map():
	render = {
		"data": flatten_data(data)
	}
	return render_template('map.html', **render)


if __name__ == "__main__":
	app.run(debug=True)
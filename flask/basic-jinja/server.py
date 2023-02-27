import os
from flask import Flask, render_template

# global variable for parent directory as app root
app_root = os.path.abspath('.') # '.' => **/server-templates/flask/basic

# flask specific directories for retrieving assets
static_folder = os.path.join(app_root, 'static') # ./static
template_folder = os.path.join(app_root, 'template') # ./template

# initialize the Flask app
app = Flask(__name__,
	static_folder=static_folder,
	template_folder=template_folder)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html') # ./template/index.html


# run Flask server when calling flask.py directly
if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port=5000,
		debug=True
	)


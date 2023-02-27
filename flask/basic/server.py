import os
from flask import Flask, render_template

# to make this more adaptable, the following will make the
# root directory of the app to the directory which it's within.
#     */server-templates/flask/basic/server.py
#     => */server-templates/flask/basic/
app_root = os.path.abspath('.')
static_folder = os.path.join(app_root, 'static')
template_folder = os.path.join(app_root, 'template')

# initialize the Flask app
app = Flask(__name__,
    static_folder=static_folder,
    template_folder=template_folder
)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# run Flask server when calling flask.py directly
if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )


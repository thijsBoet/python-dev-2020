from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/works')
def works():
    return render_template('./works.html')

@app.route('/about')
def about():
    return render_template('./about.html')

@app.route('/contact')
def contact():
    return render_template('./contact.html')

# export FLASK_APP=server.py                            set python file
# export FLASK_ENV=development                          reset to developent mode so server restarts on change
# flask run                                             run flask application

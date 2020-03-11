from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/about')
def about():
    return render_template('./about.html')


@app.route('/work')
def work():
    return render_template('./work.html')

# export FLASK_APP=server.py                            set python file
# export FLASK_ENV=development                          reset to developent mode so server restarts on change
# flask run                                             run flask application

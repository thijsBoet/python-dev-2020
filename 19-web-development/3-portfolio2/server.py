from flask import Flask, request, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submitted hooray'

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

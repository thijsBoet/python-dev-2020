from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('./thankyou.html')
    else:
        return 'Something went wrong try again'


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

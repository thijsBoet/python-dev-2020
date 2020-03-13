from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('./thankyou.html')
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

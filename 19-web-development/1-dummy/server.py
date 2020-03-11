from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('./index.htm', name=username, post_id=post_id)


@app.route('/about')
def about():
    return render_template('./about.htm')


@app.route('/blog')
def blog():
    return 'These are my thoughts on web development in Python'


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'


# export FLASK_APP=server.py                            set python file
# export FLASK_ENV=development                          reset to developent mode so server restarts on change
# flask run                                             run flask application

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Matthijs!'

# export FLASK_APP=server.py                            set python file
# export FLASK_ENV=development                          reset to developent mode so server restarts on change
# flask run                                             run flask application
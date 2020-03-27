  
import os
from flask import Flask

app = Flask(__name__)


@app.route('/') # The selected url (the root directory here) wil trigger the function below
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) # Never leave it True when relasing an app
            
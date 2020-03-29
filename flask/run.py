  
import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'abrakadabra'

@app.route('/') # The selected url (the root directory here) wil trigger the function below
def index():
    return render_template("index.html", page_title="Home")

@app.route('/about')
def about():
    data = [] # Will be filled with the content of the JSON file
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data) # {{ company }} will print data (our JSON file) on about.html

@app.route('/contact', methods=["GET", "POST"]) # Allow GET an POST methods on this page
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!" .format(request.form["name"]))

    return render_template("contact.html", page_title="Contact")

@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Carrers")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            debug=True) # Never leave it True when relasing an app

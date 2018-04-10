from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from Crime_load import crime_script

app = Flask(__name__)
app.secret_key = 'dopamin'


@app.route('/')
def my_form():
    return render_template("index.html")


@app.route('/api/<question>', methods=['GET', 'POST'])
def home(question):
    if request.method == 'POST':
        crime_api = crime_script(question)

        return jsonify(crime_api)


if __name__ == "__main__":
    app.run(debug=True)
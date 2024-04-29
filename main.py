from flask import Flask, render_template

app = Flask(__name__,)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/general/')
def general():
    return render_template('general.html')

@app.route('/reasons/')
def reasons():
    return render_template('reasons.html')

@app.route('/results/')
def results():
    return render_template('results.html')

@app.route('/chronology/')
def chronology():
    return render_template('chronology.html')

@app.route('/people/')
def people():
    return render_template('people.html')

app.run(debug=True)
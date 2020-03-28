from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    heading = 'Its HIGH NOON'
    title = 'This is Sparta'
    subtitle = 'Dig it. SUCKA!!!'
    return render_template('hello.html', Heading = heading, title = title, subtitle = subtitle)
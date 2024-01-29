from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxx"
@app.route("/")
def home():
    return ({"Message": "Hello World!"})

#Access token credentials

@app.route("/access_token")
def token():
    endpoint = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    data = (requests.get(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret))).json()
    return data




if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True, port = 5111)
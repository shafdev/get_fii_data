from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    req = requests.get('https://api.sensibull.com/v1/fii_dii_details?_=90503190003450309907')
    text = req.text
    data = json.loads(text)
    fii = data['fii_dii_data']['2021-10-01']['cash']['dii']['buy']
    print(fii)
    fii = str(fii)
    return fii
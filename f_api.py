import requests
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def shop():
    r = requests.get("https://fortnite-api.com/v2/shop/br/combined").json()
    return render_template("index.html",items=r["data"],bbuck=r["data"]["vbuckIcon"])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2233)
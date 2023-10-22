from flask import Flask , render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/weatherapp", methods = ["POST", "GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"

    param = {'q' : request.form.get("city"),
        'appid' : request.form.get("appid"),
        'units' : request.form.get("units")
    }

    reponse = requests.get(url, params = param)
    data = reponse.json()
    city = data['name']
    return f"data : {data}, city :{city}"



if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port = 8001)
from flask import Flask , render_template, request, url_for
from flask_cors import cross_origin 
import pickle
import pandas as pd


app = Flask(__name__)
model=pickle.load(open('./models/cat.pkl', 'rb'))
print('model loaded')

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predict():
    if request.method == "POST":
        #date
        date=request.form['date']
        day = float(pd.to_datetime(date, format="%Y-%m-%dT").day)
	    #month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)
        month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)

        minTem=float(request.form['mintemp'])
        maxTemp=float(request.form['maxtemp'])
        rainfall=float(request.form['rainfall'])
        evaporation=float(request.form['evaporation'])
        sunshine=float(request.form['sunshine'])
        windgustspeed=float(request.form['windgustspeed'])
        windspeed9am=float(request.form['windspeed9am'])
        windspeed3pm=float(request.form['windspeed3pm'])
        humidity9am=float(request.form['humidity9am'])
        humidity3pm=float(request.form['humidity3pm'])
        pressure9am=float(request.form['pressure9am'])
        pressure3pm=float(request.form['pressure3pm'])
        temp9am=float(request.form['temp9am'])
        temp3pm=float(request.form['temp3pm'])
        cloud9am=float(request.form['cloud9am'])
        cloud3pm=float(request.form['cloud3pm'])
        location=float(request.form['location'])
        winddir9am=float(request.form['winddir9am'])
        winddir3pm=float(request.form['winddir3pm'])
        windgustdir=float(request.form['windgustdir'])
        raintoday=float(request.form['raintoday'])

        list=[raintoday, windgustdir, winddir3pm, winddir9am, location, cloud3pm, cloud9am, temp3pm, temp9am,
                pressure3pm, pressure9am, humidity3pm, humidity9am, windspeed3pm, windspeed9am, windgustspeed, 
                sunshine, evaporation, rainfall, maxTemp, minTem, month, day]
        
        pred=model.predict(list)
        output=pred
        if output == 0:
            return render_template('noRain.html')
        else:
            return render_template('ifRain.html')
    return render_template('predict.html')

if __name__=="__main__":
    app.run(debug=True)


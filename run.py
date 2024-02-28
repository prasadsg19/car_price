from flask import Flask , request , jsonify , render_template
import pandas as pd
from utils import CarPrice

dataset=pd.read_csv(r'data/CarPrice_Assignment.csv')
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/api/fueltype')
def get_fueltype_options():
    fueltype_options = dataset['fueltype'].unique().tolist()
    return jsonify(fueltype_options)

@app.route('/api/aspiration')
def get_aspiration_options():
    aspiration_options = dataset['aspiration'].unique().tolist()
    return jsonify(aspiration_options)

@app.route('/api/doornumber')
def get_doornumber_options():
    doornumber_options = dataset['doornumber'].unique().tolist()
    return jsonify(doornumber_options)

@app.route('/api/enginelocation')
def get_enginelocation_options():
    enginelocation_options = dataset['enginelocation'].unique().tolist()
    return jsonify(enginelocation_options)


@app.route('/api/carbody')
def get_carbody_options():
    carbody_options = dataset['carbody'].unique().tolist()
    return jsonify(carbody_options)

@app.route('/api/drivewheel')
def get_drivewheel_options():
    drivewheel_options = dataset['drivewheel'].unique().tolist()
    return jsonify(drivewheel_options)

@app.route('/api/enginetype')
def get_enginetype_options():
    enginetype_options = dataset['enginetype'].unique().tolist()
    return jsonify(enginetype_options)

@app.route('/api/fuelsystem')
def get_fuelsystem_options():
    fuelsystem_options = dataset['fuelsystem'].unique().tolist()
    return jsonify(fuelsystem_options)

@app.route('/api/cylindernumber')
def get_cylindernumber_options():
    cylindernumber_options = dataset['cylindernumber'].unique().tolist()
    return jsonify(cylindernumber_options)




@app.route('/api/predict',methods=['POST'])

def model_prediction():

    fueltype=request.form['fueltype']
    aspiration=request.form['aspiration']
    doornumber=request.form['doornumber']
    enginelocation=request.form['enginelocation']
    wheelbase=request.form['wheelbase']
    carlength=request.form['carlength']
    carwidth=request.form['carwidth']
    carheight=request.form['carheight']
    curbweight=request.form['curbweight']
    cylindernumber=request.form['cylindernumber']
    enginesize=request.form['enginesize']
    boreratio=request.form['boreratio']
    stroke=request.form['stroke']
    compressionratio=request.form['compressionratio']
    horsepower=request.form['horsepower']
    peakrpm=request.form['peakrpm']
    citympg=request.form['citympg']
    highwaympg=request.form['highwaympg']
    carbody=request.form['carbody']
    drivewheel=request.form['drivewheel']
    enginetype=request.form['enginetype']
    fuelsystem=request.form['fuelsystem']

    car_price=CarPrice()


    result=car_price.get_car_price(fueltype, aspiration, doornumber, enginelocation,
       wheelbase, carlength, carwidth, carheight, curbweight,
       cylindernumber, enginesize, boreratio, stroke,
       compressionratio, horsepower, peakrpm, citympg,
       highwaympg,carbody,drivewheel,enginetype,fuelsystem)
    
    return str(result)


if __name__ == "__main__":
    app.run(port=1001,debug=False)
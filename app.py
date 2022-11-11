


from copyreg import pickle
from fileinput import filename
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

def prediction(lst):
    filename = 'model/picklefdm.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        pred_value = model.predict([lst])
        return pred_value

@app.route('/', methods=['POST','GET'])
def index():
    pred_value = 0
    if request.method == 'POST':
        
        Year = request.form['Year']
        Brand = request.form['Brand']
        Condition = request.form['Condition']
        Transmission = request.form['Transmission']
        Fuel= request.form['Fuel']
       

        # print(Price,Brand,Year,Condition,Transmission,Fuel,Mileage)
        
        feature_list = []
        feature_list.append(int(Year))
        

        Brand_list = ['Bajaj','Honda','Nissan','Other','Suzuki','Toyota']
        Condition_list = ['New','Other','Reconditioned','Used']
        Transmission_list = ['Automatic','Manual','Other','Other transmission','Tiptronic']
        Fuel_list = ['Diesel','Electric','Hybrid','Other','Petrol']
        

        def traverse(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse(Brand_list, Brand)
        traverse(Condition_list, Condition)
        traverse(Transmission_list, Transmission)
        traverse(Fuel_list, Fuel)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],2)
      


    return render_template("index.html", pred_value = pred_value)

if __name__ == '__main__' :
    app.run(debug=True)
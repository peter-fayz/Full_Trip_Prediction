import pickle
from flask import Flask , request ,jsonify
import pandas as pd
import numpy as np


model = pickle.load(open('Full_Trip_Prediction.pkl','rb'))

app = Flask(__name__)

@app.route('/api/', methods = ['POST'])

def predict () :
    data = request.get_json(force=True)

    x = pd.DataFrame(data)
    
    prediction = model.predict_proba(x)
    print(prediction)

    return jsonify( prediction.tolist())

if __name__ == '__main__' :
    try :
        app.run(port=8085, debug=True)

    except :
        print('Somthing went wrong')
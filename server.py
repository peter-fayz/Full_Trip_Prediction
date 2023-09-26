import pickle
from flask import Flask , request ,jsonify
import pandas as pd
from functools import wraps


model = pickle.load(open('Full_Trip_Prediction.pkl','rb'))

app = Flask(__name__)

def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.args.get('key') and request.args.get('key') == 'Full_Trip_Prediction':
            return view_function(*args, **kwargs)
        else:
            return jsonify(status=401)
    return decorated_function



@app.route('/api/', methods = ['POST'])
@require_appkey
def predict () :
    data = request.get_json(force=True)

    x = pd.DataFrame(data)
    
    prediction = model.predict_proba(x)

    list_of_predictoins = []

    for i in prediction :
        list_of_predictoins.append(f'Voided: {(i[0]*100).round(2)}% - Full Trip: {(i[1]*100).round(2)}%')
        #print(f'Voided: {(i[0]*100).round(2)}% - Full Trip: {(i[1]*100).round(2)}%')

    print(list_of_predictoins)
    return jsonify(list_of_predictoins)

if __name__ == '__main__' :
    try :
        app.run(port=8085, debug=True)

    except :
        print('Somthing went wrong')
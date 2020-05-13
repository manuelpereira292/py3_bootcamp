import numpy as np
from flask import Flask, render_template, url_for, redirect, request, jsonify
import pickle
import os

app = Flask(__name__)
model = None

if os.path.exists('model.pkl'):
    model = pickle.load(open('model.pkl', 'rb'))
else:
    raise Exception('No model')

# --------------------------------- Starts Dummy
@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/add/<a>/<b>')
def add(a,b):
    return str(int(a) + int(b))

# ---------------------------------- Ends Dummy

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [ int(x) for x in request.form.values()]
    X = [np.array(int_features)]
    prediction = model.predict(X)
    prediction = round(prediction[0],2)

    return render_template('index.html', 
                prediction_text="Sales sould be {}".format(prediction))
    

@app.route('/api/predict',methods = ['POST'])
def results():
    data =  request.get_json(force=True)
    #print (data)
    X = [np.array(list(data.values()))]
    prediction = model.predict(X)
    prediction = round(prediction[0],2)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run()
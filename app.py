# save this as app.py
from flask import Flask, escape, request, render_template,url_for
import pickle
import numpy as np
import os
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, num2date
from matplotlib.ticker import FuncFormatter
from fbprophet import Prophet
from datetime import datetime


app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))
port=int(os.environ.get('PORT',5000))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        date = request.form['date']

        prediction = model.predict(pd.DataFrame(date, columns = ['ds']))['yhat'][0]

        return render_template("prediction.html", prediction_text="Predicted stock price {}".format(prediction))

    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=port)

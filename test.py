from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

try:
    # Load pretrained model as clf. Try any one model. 
    clf = joblib.load("./Housing_price_model/LinearRegression.joblib")
    # clf = joblib.load("./Housing_price_model/StochasticGradientDescent.joblib")
    # clf = joblib.load("./Housing_price_model/GradientBoostingRegressor.joblib")
except Exception as e:
    print(f"Error {e}")

data = {
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":60.575
   },
   "TAX":{
      "0":112.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }
}

def scale(payload):
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

inference_payload = pd.DataFrame(data)
scaled_payload = inference_payload
prediction = list(clf.predict(scaled_payload))
print({'prediction': prediction})
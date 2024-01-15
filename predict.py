import joblib
import numpy as np

model = joblib.load('rf.pkl')

def predict_we(data):
    if model.predict([data]) == 1:
        return "rainy"
    else:
        return "sunny"
    


# print(predict(np.array([15.4,15.4,0.9,10.8,5.13,1014.97])))
import numpy as np
import pickle
import joblib


model = pickle.load(open(r'C:\Users\DELL\Desktop\OmniHealth\Kidney\Kidney_Pipeline.pkl','rb'))


def prediction(input_data):
    new_data = np.array([input_data])
    new_data = new_data.reshape(1,-1)

    pred = model.predict(new_data)
    return pred[0]



if __name__=="__main__":
    # ['blood_pressure', 'albumin', 'blood_urea', 'serum_creatinine', 'sodium', 'haemoglobin', 'packed_cell_volume', 'red_blood_cell_count', 'hypertension', 'diabetes_mellitus']
    # input_data = [ 60. ,   0. ,  27. ,   0.5, 142. ,  15.2,  40.,   5.2,   0, 0] # Chronic Kidney Dieseases
    input_data = [ 90. ,   1. ,  18. ,   1.2, 140. ,   9.7,  50.,   5.5,   0. , 0 ] # Non Chronic Diseases
    
    result = prediction(input_data)

    if (result== 0):
        print('The Person does not have a Chronic Kidney Disease')
    else:
        print('The Person has Chronic Kidney Disease')
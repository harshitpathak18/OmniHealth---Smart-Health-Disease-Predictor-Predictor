import numpy as np
import pickle

model = pickle.load(open(r'OmniHealth\HeartDisease\Heart_Diseases_pipeline.pkl','rb'))


def prediction(input_data):
    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # model = pickle.load(open('Heart_Diseases_pipeline.pkl','rb'))
    pred = model.predict(input_data_reshaped)
    
    return pred[0]


if __name__=="__main__":
    # (age	sex	cp	trestbps	chol	thalach exang	slope thal)

    # input_data = (56,   0,   0, 134, 409, 150,   1,   1,   3) # Not Heart Diseases 
    input_data = (51,   1,   3, 125, 213, 125,   1,   2,   2)  # Heart Diseases

    result = prediction(input_data)

    if (result== 0):
        print('The Person does not have a Heart Disease')
    else:
        print('The Person has Heart Disease')

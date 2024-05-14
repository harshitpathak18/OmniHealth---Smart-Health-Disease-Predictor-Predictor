import pickle

model  = pickle.load(open(r"OmniHealth\Diabetes\Diabetes_Pipeline.pkl",'rb'))

def prediction(input_data):
    import numpy as np
    
    input_data = np.array(input_data)
    X_new = input_data.reshape(1, -1)
    result = model.predict(X_new)[0]

    return result


if __name__=="__main__":
    # Pregnancies	Glucose	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	
    # input_data = [  2.   , 175.   ,  27.   , 102.5  ,  22.9  ,   0.326,  22.   ] # Not Diabetic 
    input_data = [  4.  , 117.  ,  12.  , 169.5 ,  29.7 ,   0.38,  30.  ]  # Diabetic
    
    result = prediction(input_data)
    
    print("Diabetic") if result==1 else print("Non Diabetic")

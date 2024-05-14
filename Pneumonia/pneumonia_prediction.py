import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from keras.models import load_model
import joblib
import pickle

model = load_model(r"C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia.h5")  
# model = load_model(r"C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia_new_1.h5")

def prediction(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values

    # Make the prediction
    pred = model.predict(img_array)

    return pred[0][0]

if __name__ =="__main__":
    # img_path = r"C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\6.jpeg"

    # result = prediction(img_path)
    # predicted_class = print("Pneumonia")if result > 0.5 else print('Normal')
    
    # sample = plt.imread(img_path)
    # plt.imshow(sample)
    # plt.show()

    pneumonia_img_paths = [
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\1.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\2.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\3.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\4.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\5.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\6.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\7.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\8.jpeg',        
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\9.jpeg',        
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Pneumonia\10.jpeg',        
    ]

    normal_img_paths = [
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\1.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\2.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\3.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\4.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\5.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\6.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\7.jpeg',
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\8.jpeg',        
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\9.jpeg',        
        r'C:\Users\DELL\Desktop\OmniHealth\Pneumonia\Normal\10.jpeg',        
    ]

    print("For Normal")
    for i in normal_img_paths:
        result = prediction(i)
        print(result)
        predicted_class = print("Pneumonia")if result >= 0.5 else print('Normal')
    
    
    print("\n\n\nFor Pneumonia")
    for i in pneumonia_img_paths:
        result = prediction(i)
        print(result)
        predicted_class = print("Pneumonia")if result >= 0.5 else print('Normal')
    
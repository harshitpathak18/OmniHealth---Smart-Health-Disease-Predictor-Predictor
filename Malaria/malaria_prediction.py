import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from keras.models import load_model

model = load_model(r'OmniHealth\Malaria\Malaria_94_acc.h5')  

def predict(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values

    # Make the prediction
    prediction = model.predict(img_array)

    return prediction[0][0]

if __name__ =="__main__":
    img_path = r"C:\Users\DELL\Downloads\download.jpeg"

    result = prediction(img_path)
    predicted_class = print("Malaria")if result <= 0.5 else print('Normal')

    sample = plt.imread(img_path)
    plt.imshow(sample)
    plt.show()

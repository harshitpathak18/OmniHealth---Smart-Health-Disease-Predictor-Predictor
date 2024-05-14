import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from keras.models import load_model

model = load_model(r'C:\Users\DELL\Desktop\OmniHealth\Alzheimer\Alzheimer_88_acc.h5')  

def prediction(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values

    # Make the prediction
    prediction = model.predict(img_array)

    class_labels = ["Mild Impairment", "Moderate Impairment", "No Impairment", "Very Mild Impairment"]  # List of class labels corresponding to model output

    # Convert the prediction to class labels
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    predicted_class = class_labels[predicted_class_index]


    # Print predicted class and probabilities
    print("Predicted Class:", predicted_class)
    print("Predicted Probabilities:", prediction[0])

    return predicted_class

if __name__ =="__main__":
    img_path = r"C:\Users\DELL\Desktop\OmniHealth\Alzheimer\test\Mild_Impairment\1_(2).jpg"

    print(prediction(img_path))

    sample = plt.imread(img_path)
    plt.imshow(sample)
    plt.show()

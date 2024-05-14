import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input

model = load_model(r'C:\Users\DELL\Desktop\OmniHealth\Skin_Dieseases\efficientnet_b3_final_model.h5')  


def prediction(img_path):
    img = image.load_img(img_path, target_size=(300, 300))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values

    # img_array = preprocess_input(img_array)

    # Make the prediction
    pred = model.predict(img_array)

    return pred[0][0]

if __name__ =="__main__":
    # img_path = r"C:\Users\DELL\Desktop\OmniHealth\Skin_Dieseases\benign.png"

    # result = prediction(img_path)
    # # Convert the prediction to a class label
    # predicted_class = print("Malignant")if prediction[0, 0] > 0.5 else print('Benign')

    # # predicted_class
    # print(prediction[0]*100)
    # benign_sample = imread(img_path)
    # plt.imshow(benign_sample)




    # Remove the 'groups' parameter from the DepthwiseConv2D layer configurations
    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.DepthwiseConv2D):
            layer_config = layer.get_config()
            if 'groups' in layer_config:
                del layer_config['groups']
            layer.set_config(layer_config)

    # Save the updated model
    updated_model_path = 'updated_model.h5'
    loaded_model.save(updated_model_path)


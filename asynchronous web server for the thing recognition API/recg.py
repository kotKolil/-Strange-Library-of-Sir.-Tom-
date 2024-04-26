import cv2
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
import numpy as np

model = VGG16(weights='imagenet', include_top=False)

async def detect_objects(image_path):
    img = await cv2.imread(image_path)
    img = await cv2.resize(img, (224, 224))
    
    x = await image.img_to_array(img)
    x = await np.expand_dims(x, axis=0)
    x = await preprocess_input(x)
    
    features = await model.predict(x)
    
    
    return features


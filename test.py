import tensorflow as tf 
from tensorflow.keras.models import load_model # type: ignore
import numpy as np 
import  cv2 
import os 


model = load_model(os.path.join('models','sky_puppies_detection.h5'))
image_link = input("get the link of image : ")
image_or = cv2.imread(image_link)
image = tf.image.resize(image_or, (256,256))
yhat = model.predict(np.expand_dims(image/255,0))
stat = []
if yhat < 0.5:
    print("the picture is image of sky ")
    stat = str(" sky ")
else:
    print("the picture is images of dog puppie")
    stat = str(" puppie  ")

img = cv2.imread(image_link)
cv2.imshow(f"image {stat}",img)
cv2.waitKey(0)

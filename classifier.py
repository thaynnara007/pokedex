from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import pickle
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-m', '--model', required=True, help='path to tarined model')
ap.add_argument('-l', '--labelbin', required=True, help='path to label binarizer')
ap.add_argument('-i', '--image', required=True, help='path to input image')
args = vars(ap.parse_args())

print ("[INFO] loading image...")
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# pre-process the image for classification
image = cv2.resize(image, (96,96))
image = image.astype('float') / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

print('[INFO] loading network and label binarizer....')
model = load_model(args['model'])
lb = pickle.loads(open(args['labelbin'], 'rb').read())

print('[INFO] classifying image...')
prob = model.predict(image)[0]
index = np.argmax(prob)
label = lb.classes_[index]
label = '{}: {:.2f}%'.format(label, (prob[index]* 100))
print ('[INFO] {}'.format(label))



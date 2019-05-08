import matplotlib 
matplotlib.use("Agg")

from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from pyimagesearch.smallervggnet import SmallerVGGNet
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import pickle
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument('-d','--dataset', required=True, help="path to input dataser(directory of images)")
ap.add_argument('-m', '--model', required=True, help="path to output model")
ap.add_argument('-l', '--labelbin', required=True, help="path to output label binarizer")
ap.add_argument('-p1', '--plot1', type=str, default='plot1.png', help='path to output accuracy/loss plot')
ap.add_argument('-p2', '--plot2', type=str, default='plot2.png', help='path to output accuracy/loss plot')
ap.add_argument('-p3', '--plot3', type=str, default='plot3.png', help='path to output accuracy/loss plot')
args = vars(ap.parse_args())

''' initialize the number of epochs to train for, initial learning rate,
 batch size, and image dimensions '''
EPOCHS = 100
INIT_LR = 1e-3 # the default value for the Adam optimizer
BS = 32
IMAGE_DIMS = (96,96,3)

data = []
labels = []

print ("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args['dataset'])))
random.seed(42)
random.shuffle(imagePaths)

for imagePath in imagePaths:

  image = cv2.imread(imagePath)
  image = cv2.resize(image, (IMAGE_DIMS[1], IMAGE_DIMS[0]))
  image = img_to_array(image)
  data.append(image)

  label = imagePath.split(os.path.sep)[-2]
  labels.append(label)

print('[INFO] scale the raw pixels intensities to the range [0,1]...')
data = np.array(data, dtype=float)
data = data / 255.0
labels =  np.array(labels)
print ("[INFO] data matrix: {:.2f}MB".format(data.nbytes / (1024*1000.0)))

print ("[INFO] binarizing the labels...")
lb = LabelBinarizer()
labels = lb.fit_transform(labels)

(train_x, test_x, train_y, test_y) = train_test_split(data, labels, test_size=0.2, random_state=42)

# construct the image generator for data augmentation
augmentation = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
height_shift_range=0.1, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, 
fill_mode='nearest')

print("[INFO] compiling model...")
model = SmallerVGGNet.build(width=IMAGE_DIMS[1], height=IMAGE_DIMS[0], 
depth=IMAGE_DIMS[2], classes=len(lb.classes_))
opt = Adam(lr=INIT_LR, decay=(INIT_LR/EPOCHS))
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

print("[INFO] training network...")
H = model.fit_generator(augmentation.flow(train_x, train_y, batch_size=BS),
validation_data=(test_x,test_y), steps_per_epoch=(len(train_x) // BS),
epochs=EPOCHS, verbose=1)

# saving the model to disk
print("[INFO] serializing network...")
model.save(args['model'])

#saving the label binarizer to disk
print("[INFO] serializing label binarizer...")
file = open(args['labelbin'], 'wb')
file.write(pickle.dumps(lb))
file.close()

# plot the training loss and accuracy
plt.style.use('ggplot')
plt.figure()
N = EPOCHS
arange = np.arange(0, N)
plt.plot(arange, H.history['loss'], label='train_loss')
plt.plot(arange, H.history['acc'], label='train_acc')
plt.title('Training Loss and Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss/Accuracy')
plt.legend(loc='upper left')
plt.savefig(args['plot1'])

plt.figure()
plt.plot(arange, H.history['val_loss'], label='val_loss')
plt.plot(arange, H.history['val_acc'], label='val_acc')
plt.title('Test Loss and Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss/Accuracy')
plt.legend(loc='upper left')
plt.savefig(args['plot2'])

plt.figure()
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
plt.title("All Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="upper left")
plt.savefig(args["plot3"])




from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K

class SmallerVGGNet:

  @staticmethod
  def build(width, height, depth, classes):

    #initialize the model for 'channel last' configuration
    model = Sequential()
    inputShape = (height, width, depth)
    chanDim = -1

    #initialize the model for 'channel first' configuration
    if (K.image_data_format() == 'channels_first'):
      inputShape = (depth, height, width)
      chanDim = 1

    # adding layes
    # convolution -> ReLu -> Pooling
    # 32 filters with 3x3 features
    model.add(Conv2D(32,(3,3), padding="same", input_shape=inputShape)) # 96 x 96 x 32
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.35))
    # Convolution -> ReLu -> Convolution -> ReLu -> Pooling
    model.add(Conv2D(64, (3,3), padding='same')) # 48 x48 x 64 
    model.add(Activation('relu'))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(64, (3,3), padding='same')) 
    model.add(Activation('relu'))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.45))
    # Convolution -> ReLu -> Convolution -> ReLu -> Pooling
    model.add(Conv2D(128, (3,3), padding="same")) # 24 x 24 x 128
    model.add(Activation('relu'))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(128, (3,3), padding='same'))
    model.add(Activation('relu'))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.50))
    # seting our fully connected layer
    model.add(Flatten())
    model.add(Dense(1024))
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.55))
    # softmax classifier
    model.add(Dense(classes))
    model.add(Activation('softmax'))

    return model

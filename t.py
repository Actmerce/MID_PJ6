import tensorflow as tf
import keras
import shutil
import os

from keras.applications import vgg16
from keras.layers import Input
from keras.preprocessing.image import ImageDataGenerator

input_tensor = vgg16.preprocess_input(Input((224, 224), 3))

vgg16_model = vgg16.VG16(include_top=True, weights='imagenet',
                                input_tensor=input_tensor, input_shape=None,
                                pooling=None,
                                classes=1000)
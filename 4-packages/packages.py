import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.datasets import mnist
from keras.utils import to_categorical

if __name__ == '__main__':
    # Using numpy here
    a = np.zeros((3, 3))
    print(a)

    # Using mnist from keras.datasets
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)
    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)
    print(train_images.shape)  # (60000, 28, 28, 1)
    print(train_labels.shape)  # (60000, 10)

    # Using matplotlib package
    plt.figure()
    ax = plt.subplot(2, 3, 1)
    ax.imshow(train_images[0, :, :, 0].reshape(28, 28), 'gray')
    ax = plt.subplot(2, 3, 2)
    ax.imshow(train_images[10000, :, :, 0].reshape(28, 28), 'gray')
    ax = plt.subplot(2, 3, 3)
    ax.imshow(train_images[1, :, :, 0].reshape(28, 28), 'gray')
    ax = plt.subplot(2, 3, 4)
    ax.imshow(train_images[2, :, :, 0].reshape(28, 28), 'gray')
    ax = plt.subplot(2, 3, 5)
    ax.imshow(train_images[3, :, :, 0].reshape(28, 28), 'gray')
    ax = plt.subplot(2, 3, 6)
    ax.imshow(train_images[4, :, :, 0].reshape(28, 28), 'gray')
    plt.savefig("example_images.png")
    plt.show()
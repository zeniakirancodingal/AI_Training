import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import tensorflow
from tensorflow import keras
from keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset. It contains 60000 training samples & 10000 test samples
# x_train & y_train are training datasets
# x_test & y_test are testing datasets
# x_train[i] is 28x28 array of pixel values ranging from 0-255, an image
# y_train[i] is a number from 0-9, a label
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize the data
# pixel values are divided by 255 so they fall between 0 and 1.
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
# Layer 1 flattens the 2D image into vector of 28x28 = 784 values
# ----------------------------------------------------------------
# Layer 2 is fully connected layer with 128 neurons, 
# each neuron connects to every pixel of 784 values
# ----------------------------------------------------------------
# Output layer with 10 neurons (one for each digit 0–9)
# Softmax converts raw outputs into probabilities that sum to 1

model = models.Sequential([
    layers.Flatten(input_shape = (28,28)), 
    layers.Dense(128, activation="relu"), 
    layers.Dense(10, activation="softmax")
    ])

# Compile the model
# "Adam" is an optimizer that adapts the learning rate automatically for each parameter.
# "sparse_categorical_crossentropy" measures how wrong predictions are
#  metrics=['accuracy'] displays accuracy after each epoch
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
# epochs = 5 means that see the training data 5 times 
model.fit(x_train, y_train, epochs=5)

# Evaluate the model & print accuracy
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_test)

# Display any image and make prediction
plt.imshow(x_test[10], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[10].argmax()}")
plt.show()

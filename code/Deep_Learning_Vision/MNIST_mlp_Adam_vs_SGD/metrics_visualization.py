import tensorflow as tf
import tensorflow.keras.datasets as ds
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam, SGD

(x_train, y_train), (x_test, y_test)= ds.mnist.load_data()
x_train = x_train.reshape(60000,784)
x_test = x_test.reshape(10000,784)
x_train = x_train.astype(np.float32)/255.0
x_test = x_test.astype(np.float32)/255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

mlp_SGD = Sequential()
mlp_SGD.add(Dense(units=512, activation='tanh', input_shape=(784,)))
mlp_SGD.add(Dense(units=10, activation='softmax'))

mlp_SGD.compile(loss='MSE', optimizer=SGD(learning_rate=0.01),
            metrics=['accuracy'])
hist_mlp_SGD = mlp_SGD.fit(x_train,y_train,batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=2)
print('SGD 정확률=',mlp_SGD.evaluate(x_test, y_test, verbose=0)[1]*100)



mlp_adam = Sequential()
mlp_adam.add(Dense(units=512, activation='tanh', input_shape=(784,)))
mlp_adam.add(Dense(units=10, activation='softmax'))

mlp_adam.compile(loss='MSE', optimizer=Adam(learning_rate=0.001),
            metrics=['accuracy'])
hist_mlp_adam = mlp_adam.fit(x_train,y_train,batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=2)
print('Adam 정확률=',mlp_adam.evaluate(x_test, y_test, verbose=0)[1]*100)

import matplotlib.pyplot as plt
plt.plot(hist_mlp_SGD.history['accuracy'], 'r--')
plt.plot(hist_mlp_SGD.history['val_accuracy'], 'r')
plt.plot(hist_mlp_adam.history['accuracy'], 'b--')
plt.plot(hist_mlp_adam.history['val_accuracy'], 'b')
plt.title('Compoarision of SGD and Adam optimizers')
plt.ylim((0.7,1.0))
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(['train_sgd', 'val_sgd', 'train_adam', 'val_adam'])
plt.grid()
plt.show()


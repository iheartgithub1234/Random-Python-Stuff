import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5], dtype=float)
y = np.array([-1, 1, 3, 5, 7, 9], dtype=float)  # y = 2x - 1

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.01), loss='mean_squared_error')

history = model.fit(x, y, epochs=10, verbose=0)

print("Model predictions after training:")
print(model.predict(x))

plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss Over Time')
plt.show()
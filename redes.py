import tensorflow as tf

model = tf.keras.models.Sequential()
model.add(
    tf.keras.layers.Dense(16,
                          activation='relu',
                          input_shape=(2,)
                          ))
model.add(
    tf.keras.layers.Dense(3,
                          activation='relu',
                          ))

print(model.summary())
print(model.weights)

model.compile(
    loss='mean_squared_error',
    optimizer=tf.keras.optimizers.Adam(0.00001)
)


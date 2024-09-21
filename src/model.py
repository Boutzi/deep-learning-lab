from tensorflow.keras import layers, models

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(units=3, input_shape=[1], activation='relu'))
    model.add(layers.Dense(units=64, activation='relu'))
    model.add(layers.Dense(units=1))  # Output layer
    model.compile(optimizer='adam', loss='mse')
    return model

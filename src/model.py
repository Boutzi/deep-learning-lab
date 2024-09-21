from keras import Sequential, layers, Input

def build_model():
    model = Sequential()
    model.add(Input(shape=(1,)))
    model.add(layers.Dense(units=3))
    model.add(layers.Dense(units=64))
    model.add(layers.Dense(units=1))
    model.compile(optimizer='adam', loss='mse')
    return model

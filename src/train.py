import os
import json
import numpy as np
from data_loader import load_data
from model import build_model
from tensorflow.keras.models import load_model

training_name = "apprentissage de x * 2"
json_file = "c:/Users/Boutzi/Documents/Work/Dev/Git/deep-learning-lab/data/processed/training_info.json"

def update_training_info(new_epochs):
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            training_info = json.load(f)
    else:
        training_info = {
            "training": training_name,
            "epochs": 0
        }
    training_info["epochs"] += new_epochs
    with open(json_file, 'w') as f:
        json.dump(training_info, f, indent=4)

    print(f"Total epochs for '{training_info['training']}': {training_info['epochs']}")

def continue_training(model):
    train_data_input, train_data_output = load_data()
    train_data_input = np.array(train_data_input).reshape(-1, 1)
    train_data_output = np.array(train_data_output).reshape(-1, 1)

    new_epochs = 1000
    model.fit(x=train_data_input, y=train_data_output, epochs=new_epochs)

    update_training_info(new_epochs)
    model.save("c:/Users/Boutzi/Documents/Work/Dev/Git/deep-learning-lab/saved_models/my_model.keras")

def train():
    train_data_input, train_data_output = load_data()
    train_data_input = np.array(train_data_input).reshape(-1, 1)
    train_data_output = np.array(train_data_output).reshape(-1, 1)

    model = build_model()
    model.fit(x=train_data_input, y=train_data_output, epochs=1000)
    model.save("c:/Users/Boutzi/Documents/Work/Dev/Git/deep-learning-lab/saved_models/my_model.keras")
    update_training_info(1000) 

    return model

if __name__ == "__main__":
    model_path = "c:/Users/Boutzi/Documents/Work/Dev/Git/deep-learning-lab/saved_models/my_model.keras"
    if os.path.exists(model_path):
        model = load_model(model_path)
        print("Model loaded.")
        continue_training(model) 
    else:
        model = train()
        print("Model trained.")

    while True:
        x = int(input("Number: "))
        prediction = model.predict(np.array([[x]]))
        print(f"Predict: {prediction[0][0]}")

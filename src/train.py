from data_loader import load_data
from model import build_model

def train():
    # Load and preprocess data
    train_data, train_labels = load_data()

    # Build model
    model = build_model()

    # Train model
    model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_split=0.2)

    # Save the trained model
    model.save('../saved_models/my_model.h5')

if __name__ == "__main__":
    train()

import numpy as np
import tensorflow as tf

# Load a simple neural network model
def load_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation="relu", input_shape=(5,)),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy")
    return model

# Generate a sample input for prediction
def generate_input():
    return np.random.rand(1, 5)

# Perform inference using the model
def run_inference():
    model = load_model()
    sample_input = generate_input()
    prediction = model.predict(sample_input)
    print(f"Sample Input: {sample_input}")
    print(f"Model Prediction: {prediction}")

if __name__ == "__main__":
    print("Starting AI Model Inference...")
    run_inference()

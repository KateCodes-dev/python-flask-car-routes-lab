
from flask import Flask

# Initialize the Flask application.
app = Flask(__name__)

# List of existing car models used by the lab tests.
existing_models = ["Crossroads"]


# Default route: display the welcome message.
@app.route("/")
def home():
    return "Welcome to Flatiron Cars"


# Model route: check whether the requested model exists.
@app.route("/<model>")
def car_model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"

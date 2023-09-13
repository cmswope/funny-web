from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Which body part does a programmer know best? ARM",
    "How do you get the code for the bank vault? You checkout their branch."
]

@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"
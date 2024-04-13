# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

LLM_API_URL = "https://therapy-model-lzd1.onrender.com"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    data = {"prompt": prompt}
    response = requests.post(LLM_API_URL, json=data)
    generated_text = response.json()["response"]
    return generated_text

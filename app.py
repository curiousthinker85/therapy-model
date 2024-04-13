# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

LLM_API_URL = "http://localhost:8000/generate"

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
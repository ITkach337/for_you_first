from flask import Flask, json, request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
<<<<<<< HEAD
    return '<h1>Hello men img="1.jpg"</h1>'

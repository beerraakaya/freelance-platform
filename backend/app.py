from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from config import Config
from database import db
from models.user import User
from routes.user_routes import user_routes

app=Flask(__name__)

CORS(app)
app.config.from_object(Config)

app.register_blueprint(user_routes)

db.init_app(app)

with app.app_context():
    db.create_all()



@app.route('/')
def home():
    return jsonify(message="Freelance platform backend'e hoşgeldin ")

if __name__=='__main__':
    app.run(debug=True)
from flask import Blueprint, jsonify
from database import db
from models import User

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/api/users')
def get_users():
    try:
        users_list=User.query.all()
        
        users_json=[]
        for user in users_list:
            users_json.append({
                'id': user.id,
                'username': user.username,
                'email': user.email
            })

        return jsonify(users=users_json)
    except Exception as e:
        return jsonify(error=str(e)), 500
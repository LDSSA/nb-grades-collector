from flask import request, Blueprint, jsonify
from src.schema import SlackUser
from src.config import DB

"""
endpoints related with account creation

Endpoints:
    ->create_users;
    ->get_users; Todo
    ->update slack username
"""

# TODO include login
create_users = Blueprint('create_users', __name__)

@create_users.route('/create_users', methods=['POST'])
def _create():
    """
    Creation of an user
    Return a success message
    The request should follow the structure bellow:
    {
    "users": [{"slack_id": int,
                "slack_username": str,
                "email": str,
                "password": str},
                {...},
                ...
            ]
    }
    """
    # TODO only allow user creation if is an admin user
    try:
        obs_dict = request.get_json()
        users = obs_dict["users"]
        for user in users:
            slack_id = user["slack_id"]
            slack_username = user["slack_username"]
            email = user["email"]
            password = user["password"]
            user = SlackUser(slack_id=slack_id,
                             slack_username=slack_username,
                             email=email,
                             password=password)
            user.save()
        response = {"status": "ok", "details": None}
        return jsonify(response)
    except Exception as e:
        DB.rollback()
        response = {"status": "error", "details": None}
        return jsonify(response)

# TODO include login
update_info = Blueprint('update_info', __name__)

@update_info.route('/update_info', methods=['POST'])
def _update_info():
    """
    Creation of an user
    Return a success message
    The request should follow the structure bellow:
    {
    "users" = [{"slack_id": int,
                "slack_username": str,
                "email": str,
                "password": str},
                {...},
                ...
            ]
    }
    """
    # TODO only allow user creation if is an admin user
    try:
        obs_dict = request.get_json()
        users = obs_dict["users"]
        for user in users:
            slack_id = user["slack_id"]
            user = SlackUser.get(slack_id==slack_id)
            user.slack_username = user["slack_username"]
            user.email = user["email"]
            user.save()
        response = {"status": "ok", "details": None}
        return jsonify(response)
    except:
        DB.rollback()
        response = {"status": "error", "details": None}
        return jsonify(response)

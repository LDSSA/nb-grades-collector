from flask import request, Blueprint, jsonify
from schema import SlackUser
from config import DB

"""
endpoints related with account creation

Endpoints:
    ->create_user;
"""

# TODO include login
create_users = Blueprint('create_user', __name__)

@create_users.route('/create_user', methods=['POST'])
def _create():
    """
    Creation of an user
    Return a success message
    The request should follow the structure bellow:
    {"slack_id": "78",
    "slack_username": "slack_username",
    "email": "email"}
    """
    # TODO only allow user creation if is an admin user
    try:
        obs_dict = request.get_json()

        slack_id = obs_dict["slack_id"]
        slack_username = obs_dict["slack_username"]
        email = obs_dict["email"]
        user = SlackUser(slack_id=slack_id,
                         slack_username=slack_username,
                         email=email
        )
        user.save()
        response = {"status": "ok", "details": None}
        return jsonify(response)
    except Exception as e:
        DB.rollback()
        response = {"status": "error", "details": None}
        return jsonify(response)


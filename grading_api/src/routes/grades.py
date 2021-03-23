from flask import request, Blueprint, jsonify
from schema import SlackUser, Grade
from config import DB

"""
endpoints related with account creation

Endpoints:
    ->register_grade;
"""

register_grade = Blueprint('register_grade', __name__)


@register_grade.route('/register_grade', methods=['POST'])
def _register_grade():
    """
    Registration of a Grade
    Return a success message
    The request should follow the structure bellow:
    {
    "slack_id": "78",
    "slu": "slu0",
    "grade": 16
    }
    """
    try:
        obs_dict = request.get_json()
        slack_id = obs_dict["slack_id"]
        slu = obs_dict["slu"]
        last_grade = obs_dict["grade"]
        user = SlackUser.get_or_none(slack_id=slack_id)
        if not user:
            raise ValueError(f"User with slack id {slack_id} does not exist")
        slack_id = user.slack_id
        grade = Grade.get_or_none(slack_id=slack_id, slu=slu)
        if not grade:
            grade = Grade(slack_id=slack_id, slu=slu, grade=last_grade, highest_grade=last_grade)
        elif grade.highest_grade < last_grade:
            grade.highest_grade = last_grade
            grade.grade = last_grade
        else:
            grade.grade = last_grade
        grade.save()
        response = {"status": "ok", "details": None}
        return jsonify(response)
    except Exception as e:
        DB.rollback()
        response = {"status": "error", "details": None}
        return jsonify(response)

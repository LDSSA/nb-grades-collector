from flask import request, Blueprint, jsonify
from src.schema import SlackUser, Grade
from src.config import DB

"""
endpoints related with account creation

Endpoints:
    ->register_grade;
    ->get_grades_by_slu;
"""

# TODO include login
register_grade = Blueprint('register_grade', __name__)


@register_grade.route('/register_grade', methods=['POST'])
def _register_grade():
    """
    Registation of a Grade
    Return a success message
    The request should follow the structure bellow:
    {"email": str,
    "slu": str,
    "utils": int
    }
    """
    try:
        obs_dict = request.get_json()
        email = obs_dict["email"]
        slu = obs_dict["slu"]
        last_grade = obs_dict["utils"]
        user = SlackUser.get_or_none(email=email)
        if not user:
            raise ValueError(f"User with email {email} does not exist")
        user_id = user.id
        grade = Grade.get_or_none(user_id=user_id, slu=slu)
        if not grade:
            grade = Grade(user_id=user_id, slu=slu, grade=last_grade, highest_grade=last_grade)
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
        response = {"status": "error", "details": e}
        return jsonify(response)

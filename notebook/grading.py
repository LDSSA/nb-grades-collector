import requests
import nbformat
from nbgrader import utils
import json

API_URL = "https://sub-nb-grades-collector.herokuapp.com"


def get_grade(notebook_path):
    nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
    total_score = 0
    max_total_score = 0
    for cell in nb.cells:
        if utils.is_grade(cell):
            score, max_score = utils.determine_grade(cell)
            total_score += score
            max_total_score += max_score
    return total_score, max_total_score


def submit_grade(slack_id: str, slack_username: str, email: str,
           grade: int, max_grade: int, learning_unit: int) -> None:
    '''
    Submits the notebook to the grades-collector.

    param slack_id like "UTS63FC02"
    param slack_username like "my_username"
    param email like "my_email@email.com"
    param learning_unit like 0
    '''
    data = {
        "learning_unit": learning_unit,
        "slack_id": slack_id,
        "grade": grade,
        "metadata": {"slack_username": slack_username,
                     "email": email,
                     "max_grade": max_grade}
    }
    print(json.dumps(data))
    response = requests.put(
        "https://sub-nb-grades-collector.herokuapp.com/submit",
        data=json.dumps(data)
    )
    print('Success' if response.ok else 'Whoopsie Daisy')

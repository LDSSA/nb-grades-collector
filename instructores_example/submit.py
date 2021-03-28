import requests
import nbformat
from nbgrader import utils
import json

API_URL = "https://sub-nb-grades-collector.herokuapp.com"
NOTEBOOk_PATH = "Exercises Notebook.ipynb"


def _get_grade(notebook_path):
    nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
    total_score = 0
    max_total_score = 0
    for cell in nb.cells:
        if utils.is_grade(cell):
            score, max_score = utils.determine_grade(cell)
            total_score += score
            max_total_score += max_score
    return int(total_score), int(max_total_score)


def submit(slack_id: str, learning_unit: int) -> None:
    '''
    Submits the notebook to the grades-collector.

    param slack_id like "UTS63FC02"
    param learning_unit like 0
    '''
    try:
        total_score, max_total_score = _get_grade(NOTEBOOk_PATH)
        assert isinstance(total_score, int)
        print(f"Your grade is {total_score} out of {max_total_score}!")
    except:
        print("Error while calculating your grade!")
        return None
    print("...Sending Grade...")
    data = {
        "learning_unit": learning_unit,
        "slack_id": slack_id,
        "grade": total_score,
        "metadata": {}
    }
    response = requests.put(
        f"{API_URL}/submit",
        data=json.dumps(data)
    )
    print('Your grade was successfully submitted!' if response.ok else 'Error while submitting your grade!')
    return None

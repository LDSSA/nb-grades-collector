import nbformat
from nbgrader import utils
import requests
import json

API_ROUTE = "http://localhost:5000/"


def grade(notebook_path):
    # TODO check the edge case when the notebook is not executed
    # TODO check percentage of exercises passed
    nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
    total_score = 0
    max_total_score = 0
    for cell in nb.cells:
        if utils.is_grade(cell):
            score, max_score = utils.determine_grade(cell)
            total_score += score
            max_total_score += max_score
    return total_score, max_total_score


def register_slack_account():
    slack_id = input("Please create an account. Type your slack Member ID.")
    slack_id = str(slack_id.strip())
    print(f"Slack id: {slack_id}")
    slack_username = input("Type your slack username.")
    slack_username = str(slack_username.strip())
    print(f"Slack username: {slack_username}")
    email = input("Type your email.")
    email = str(email.strip())
    print(f"Email: {email}")
    headers = {'Content-Type': 'application/json'}
    body = json.dumps({"slack_id": slack_id, "slack_username": slack_username, "email": email})
    url = f'{API_ROUTE}create_user'
    json_response = requests.request("POST", url=url, headers=headers, data=body).json()
    if json_response["status"] == "ok":
        return slack_id
    else:
        print(">>Error: Something went wrong while creating your account!\n",
              "\t1)Please check if your account already exists.\n",
              "\t2)Check it by  answering 'y' to the question 'Did you already submit your account on the grading system?'.\n",
              "\3)Continue with the grading process, if everything goes well means that your account was already created.")
        return None


def login():
    # Todo handle cases where the user try to register a member id that already exists!
    execute = input("Did you executed all the cells above? y/n:")
    if execute != "y":
        print("Please execute all the cells above before continuing or type y.")
        return None
    save = input("Did you saved the notebook? y/n:")
    if save != "y":
        print("Please execute all the cells above before continuing or type y.")
        return None
    have_account = input("Did you already submit your account on the grading system? y/n")
    if have_account != "y":
        print("Let's register your account!")
        slack_id = register_slack_account()
        return slack_id
    elif have_account == "y":
        slack_id = input("Type your slack Member ID.")
        slack_id = slack_id.strip()
        print(f"Slack id: {slack_id}")
        return slack_id
    else:
        print("Please create an account or type y!")
        return None


def send_grade(slack_member_id, slu):
    total_score, max_total_score = grade("Exercises Notebook.ipynb")
    endpoint = "register_grade"
    body = json.dumps({"slack_id": slack_member_id, "grade": total_score, "slu": slu})
    url = f'{API_ROUTE}/{endpoint}'
    headers = {'Content-Type': 'application/json'}
    json_response = requests.request("POST", url=url, headers=headers, data=body).json()
    if json_response["status"] == "ok":
        print(f"Your grade is {total_score} out of {max_total_score}!")
        return total_score
    else:
        print(">>Error: Something went wrong while sending your grade.\n",
              "Please make sure you:\n",
              "\t1) Save the notebook before running this cell;\n",
              "\t2) Your member id is registered in the system;\n",
              "\t3) You wrote your member id correctly.")
        return None

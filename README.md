# nb-grades-collector

## use Jupyter notebook

1. Copy the `submit.py` file to the same folder as the Exercise Notebook.
2. Install and add `requests` to the requirements file

```bash
pip install requests
pip freeze > requirements.txt
```

To submit a LU you'll need to add 3 cells at the bottom of the notebook, as follows:

<img src='assets/submit.png' alt='Finder' width="75%" />

**Cell 1** markdown, read-only
```markdown
# Sumit your work!

To submit your work, [get your slack id](https://moshfeu.medium.com/how-to-find-my-member-id-in-slack-workspace-d4bba942e38c) and fill it in the `slack_id` variable.

Example: `slack_id = "UTS63FC02"`
```

**Cell 2** code, Autograded Answer
```python
slack_id = None
```

**Cell 3** code, Autograded tests
```python
from submit import submit

submit(slack_id, 0)
```

This serves to collect the student slack ids so that we know hwo has submitted the LU.

## use with curl

```bash
curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"learning_unit": 0,"slack_id":"UTS63FC02","grade": 0,"metadata":{}}' \
  http://localhost:8000/submit

curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"learning_unit": 0,"slack_id":"UTS63FC02","grade": 0,"metadata":{}}' \
  http://localhost/submit

curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"learning_unit": 0,"slack_id":"UTS63FC02","grade": 0,"metadata":{}}' \
  https://sub-nb-grades-collector.herokuapp.com/submit
```

## gvnicorn local run

```bash
uvicorn main:app --reload
```

## docker local run

```bash
docker build -t nb-grades-collector .
docker run --rm -it -p 80:80 nb-grades-collector
```

## deployment

```bash
heroku stack:set heroku-20
heroku git:remote -a sub-nb-grades-collector
heroku stack:set container
git push heroku mvp:main
```

## docs

```bash
https://sub-nb-grades-collector.herokuapp.com/docs
```

## postgres connect

```bash
heroku pg:psql
```

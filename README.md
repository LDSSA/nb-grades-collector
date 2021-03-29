# For Instructors

## use Jupyter notebook

1. Copy the `instructores_example/submit.py` file to the same folder as the Exercise Notebook.
2. Install the requirements on this repo

```bash
cd nb-grades-collector
cd instructores_example
pip install -r requirements.txt
```

3. Update the requirements of the LU you're working on

```bash
cd Week\ 00/SLU00\ -\ Jupyter\ Notebook/
pip freeze > requirements.txt
```

4. To enable students to submit a SLU, please copy the cells regarding work submission on `instructores_example/Exercise Notebook.ipynb`, to yours.

<img src='assets/submit.png' alt='Finder' width="75%" />


This serves to collect the student slack ids so that we know who has submitted the LU.

# For Maintainers

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
git push heroku <branch>:main
```

## docs

```bash
https://sub-nb-grades-collector.herokuapp.com/docs
```

## postgres connect

```bash
heroku pg:psql
```

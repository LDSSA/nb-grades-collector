# nb-grades-collector

## use Jupyter notebook

To submit a LU

```python
from submit import submit

slack_id = None  # example: "UTS63FC02"
assert slack_id is not None
submit(slack_id, 0)
```

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

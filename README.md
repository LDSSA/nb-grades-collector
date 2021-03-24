# nb-grades-collector

## use

```bash
curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"learning_unit": 0,"slack_id":"UTS63FC02","grade": 0,"metadata":{}}' \
  http://localhost:8000/submit
```

## deployment

```bash
git clone --single-branch --branch mvp git@github.com:LDSSA/nb-grades-collector.git
heroku git:remote -a sub-nb-grades-collector
heroku stack:set container
git push heroku HEAD:master
```

from typing import Dict
import os

from fastapi import FastAPI, Body
from pydantic import BaseModel
from peewee import (
    Model, IntegerField, TextField, CompositeKey, IntegrityError
)
from playhouse.postgres_ext import JSONField
from playhouse.db_url import connect

DB = connect(os.environ.get('DATABASE_URL') or 'sqlite:///Submissions.db')


class Submission_api(BaseModel):
    learning_unit: int
    slack_id: str = Body(..., min_length=5, max_length=20)
    grade: int
    metadata: Dict[str, str]


class Submission_db(Model):
    learning_unit = IntegerField()
    slack_id = TextField()
    grade = IntegerField()
    metadata = JSONField()

    class Meta:
        database = DB
        primary_key = CompositeKey('learning_unit', 'slack_id')


DB.create_tables([Submission_db], safe=True)

app = FastAPI()


@app.put("/submit")
def submit(
    submission_api: Submission_api
):
    submission_db = Submission_db(
        learning_unit=submission_api.learning_unit,
        slack_id=submission_api.slack_id,
        grade=submission_api.grade,
        metadata=submission_api.metadata
    )
    try:
        submission_db.save(force_insert=True)
    except IntegrityError:
        # no ned to do anyhting, means the student has already submited
        DB.rollback()

    return 'OK'

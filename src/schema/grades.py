from src.config import DB
from peewee import Model, TextField, PrimaryKeyField, IntegerField, DateTimeField

"""
schema of table utils
"""

class Grade(Model):
    id = PrimaryKeyField()
    user_id = IntegerField()
    slu = TextField()
    grade = IntegerField()
    highest_grade = IntegerField()
    # TODO date = DateTimeField()
    class Meta:
        database = DB
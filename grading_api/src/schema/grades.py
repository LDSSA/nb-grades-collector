from config import DB
from peewee import Model, TextField, PrimaryKeyField, IntegerField

"""
schema of table utils
"""

class Grade(Model):
    id = PrimaryKeyField()
    slack_id = TextField() #todo replace with slack id
    slu = TextField()
    grade = IntegerField()
    highest_grade = IntegerField()
    # TODO date = DateTimeField()
    class Meta:
        database = DB
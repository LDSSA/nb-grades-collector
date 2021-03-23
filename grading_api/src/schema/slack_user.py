from config import DB
from peewee import Model, TextField, PrimaryKeyField, IntegerField, BooleanField

"""
schema of table user
"""

class SlackUser(Model):
    slack_id = TextField(unique=True)
    slack_username = TextField(unique=True)
    email = TextField(unique=True)
    #TODO INCLUDE AN AUTENTICATION STEP! The first time password should be sent on slack!
    # TODO The user should do a registration
    class Meta:
        database = DB
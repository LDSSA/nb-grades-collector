import os
from playhouse.db_url import connect

DB = connect('sqlite:///resources/predictions.db')

#DB = connect(os.environ.get('DATABASE_URL'))
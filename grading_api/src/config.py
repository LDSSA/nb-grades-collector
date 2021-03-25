import os
from playhouse.db_url import connect

#local
DB = connect('sqlite:///resources/predictions.db')

#server
#DB = connect(os.environ.get('DATABASE_URL'))
from .slack_user import SlackUser
from .grades import Grade
from config import DB

DB.create_tables([SlackUser, Grade], safe=True)
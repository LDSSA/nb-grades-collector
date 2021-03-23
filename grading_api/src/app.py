from flask import Flask
from routes import register_grade, create_users, update_info


app = Flask(__name__)


app.register_blueprint(register_grade)
app.register_blueprint(create_users)
app.register_blueprint(update_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

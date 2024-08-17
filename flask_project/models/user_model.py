
from werkzeug.security import check_password_hash

users = [
    {"username": "admin", "password": "123"}
]

def get_user_by_username(username):
    for user in users:
        if user["username"] == username:
            return user
    return None
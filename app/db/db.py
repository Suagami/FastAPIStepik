from models.models import User, Role

USER_DATA = {}


def get_user(username: str) -> User | None:
    if username in USER_DATA:
        return User(**USER_DATA[username])
    return None
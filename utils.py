import random
from uuid import uuid4


def generate_code():
    code = random.randint(1000, 9999)
    return code


def generate_token():
    token = uuid4()
    return token
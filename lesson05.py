def email_validation(email):
    def wrapper(func):
        if '@' in email and '.' in email and email[-1] != '.':
            code = generate_code(1)
            func(email, code)
        else:
            raise Exception("Invalid email!")

    return wrapper

def generate_code(id):
    code = str(id).zfill(4)
    return code

from random import randint


def generate_code():
    code = []

    for i in range(6):
        code.append(str(randint(1, 9)))

    return str(''.join(code))

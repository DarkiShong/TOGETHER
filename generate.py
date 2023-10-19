import random


def generate_example(n):
    data = []
    operation = ['+', '*', '/', '-']
    for i in range(n):
        a = random.choice(operation)
        if a == '+' or a == '-':
            b = str(random.randint(0, 1000)) + a + str(random.randint(1, 1000))
            data.append(b)
        else:
            b = str(random.randint(0, 100)) + a + str(random.randint(1, 100))
            data.append(b)

    return data
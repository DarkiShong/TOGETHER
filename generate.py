import random


def generate_example(n, d, num_of_numbs):
    data = []
    if d == 1:
        operation = ['+', '-']
    else:
        operation = ['+', '*', '/', '-']
    for i in range(n):
        if '*' not in operation:
            b = ''
            for j in range(num_of_numbs):
                b = b + str(random.randint(0, 1000))
                if j != num_of_numbs:
                    b += str(random.choice(operation))
            data.append(b)
        else:
            b = ''
            for j in range(num_of_numbs):
                b = b + str(random.randint(1, 100))
                if j != num_of_numbs:
                    b += str(random.choice(operation))
            data.append(b)

    return data


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
                a = random.randint(-100, 100)
                if a < 0:
                    a = '(' + str(a) + ')'
                b = b + str(a)
                if j != num_of_numbs - 1:
                    b += str(random.choice(operation))
            data.append(b)
        else:
            b = ''
            for j in range(num_of_numbs):
                a = random.randint(-10, 10)
                while a != 0:
                    a = random.randint(-10, 10)

                if a < 0:
                    a = '(' + str(a) + ')'
                b = b + str(a)
                if j != num_of_numbs - 1:
                    b += str(random.choice(operation))
            data.append(b)

    return data


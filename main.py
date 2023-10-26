from generate import generate_example


name = input("Your name is:\n")
                            

while True:
    try:
        d = int(input("Enter difficulty level (1 or 2)\n"))
        break
    except ValueError:
        print("Oops!  Use onlu numbers.  Try again...")


while True:
    try:
        kolnum = int(input("How many numbers in tasks do u want:\n"))
        break
    except ValueError:
        print("Oops!  Use onlu numbers.  Try again...")


while True:
    try:
        kol = input("How many tasks do you want to solve:\n")
        break
    except ValueError:
        print("Oops!  Use onlu numbers.  Try again...")

c = generate_example(kol, d)
for i in range(0, kol):
    print(c[i])
    a = int(input())
    if a == eval(c[i]):
        print("GREAT JOB")
    else:
        print("LOOSER")

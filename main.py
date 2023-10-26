from generate import generate_example


name = input("Your name is:\n")
                            

while True:
    try:
        d = int(input("Enter difficulty level (1 or 2)\n"))
        if d == 1 or d == 2:
            break
        else:
            print("Oops!  Use onlu 1 or 2.  Try again...")
    except ValueError:
        print("Oops!  Use onlu 1 or 2.  Try again...")


while True:
    try:
        kolnum = int(input("How many numbers in tasks do u want:\n"))
        break
    except ValueError:
        print("Oops!  Use onlu numbers.  Try again...")


while True:
    try:
        kol = int(input("How many tasks do you want to solve:\n"))
        break
    except ValueError:
        print("Oops!  Use onlu numbers.  Try again...")

b = 0

c = generate_example(kol, d, kolnum)

for i in range(0, kol):
    print(c[i])
    while True:
        try:
            a = int(input())
            break
        except ValueError:
            print("Oops!  Use onlu numbers.  Try again...")
    if a == eval(c[i]):
        print("GREAT JOB")
        b += 1
    else:
        print("LOOSER","RIGHT QWESTION WAS:",eval(c[i]))
print("Right qwestions:\n",b,"/",kol)
print("Prosent:\n",round((b/kol)*100))
if (b/kol) * 100 >=50 :
    print("U're AWESOME")
elif (b/kol) * 100 < 50 and (b/kol) * 100>0:
    print("TRY AGAIN")
elif (b/kol) * 100 == 0:
    print("KILL YOUR SELF")
from generate import generate_example


name = input("Your name is:\n")
                            

while True:
    try:
        d = int(input("Enter difficulty level (1 or 2):\n"))
        if d == 1 or d == 2:
            break
        else:
            print("Oops!  Use onlu 1 or 2.  Try again...")
    except ValueError:
        print("Oops!  Use onlu 1 or 2.  Try again...")


while True:
    try:
        kolnum = int(input("Enter how many numbers do u want see in qwestion:\n"))
        if 10 >= kolnum > 0:
            break
        else:
            print("Oops!  Use number > or = 0 and numbers < or = 10.  Try again...")
    except ValueError:
        print("Oops!  Use number > or = 0 and numbers < or = 10.  Try again...")

while True:
    try:
        kol = int(input("Enter how many qwestions do u want solve:s\n"))
        if 100 >= kol > 0:
            break
        else:
            print("Oops!  Use number > or = 0 and number < or = 100.  Try again...")
    except ValueError:
        print("Oops!  Use number > or = 0 and numbers < or = 10.  Try again...")

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
elif 0 < (b/kol) * 100 < 50:
    print("TRY AGAIN")
elif (b/kol) * 100 == 0:
    print("KILL YOUR SELF")
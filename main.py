from generate import generate_example


name = input("Your name is:")
print("How many tasks do you want to solve:")
kol = int(input())

c = generate_example(kol)
for i in range (0, kol):
    print(c[i])
    a = int(input())
    if a == eval(c[i]):
        print("GREAT JOB")
    else:
        print("LOOSER")

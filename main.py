from generate import generate_example


name = input("Your name is:")
d = 0
while d != '1' and d != '2':
    print("Enter difficulty level (1 or 2)")
    d = input()

print("How many tasks do you want to solve:")
kol = int(input())

c = generate_example(kol, d)
for i in range(0, kol):
    print(c[i])
    a = int(input())
    if a == eval(c[i]):
        print("GREAT JOB")
    else:
        print("LOOSER")

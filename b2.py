n = int(input("Ex2: "))
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("False")
        break
    else:
        print("True")
        break
if n == 1 or n == 0:
    print("False")
if n == 2 or n == 3:
    print("True")
n = int(input("Ex23: "))
s = []
for i in range(1, n):
    s.append(i)
    if sum(s) >= n:
        break
s.pop(-1)
print(s)
print(max(s))
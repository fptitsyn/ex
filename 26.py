f = open("26.txt")
k = int(f.readline())
n = int(f.readline())

a = []
for i in range(n):
    st, end = map(int, f.readline().split())
    a.append([st, end])

a.sort()

c = 0
last = 0
cells = [-1] * k

for i in range(n):
    st, end = a[i]
    for j in range(k):
        if st > cells[j]:
            cells[j] = end
            c += 1
            if st != a[i - 1][0]:
                last = j + 1
            break

print(c, last)

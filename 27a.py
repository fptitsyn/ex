f = open("27b.txt")

k = int(f.readline())
n = f.readline()

a = [int(i) for i in f]
ms = 0

for i in range(len(a) - k - 1):
    for j in range(i + k, len(a)):
        ms = max(ms, a[i] + a[j])

print(ms)

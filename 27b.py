f = open("27b.txt")

k = int(f.readline())
n = int(f.readline())

a = [int(i) for i in f]

ms = 0
m_el = 0

for i in range(n - k - 1, -1, -1):
    m_el = max(a[i + k], m_el)
    ms = max(ms, a[i] + m_el)

print(ms)

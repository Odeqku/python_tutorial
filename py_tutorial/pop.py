#!/usr/bin/python3
def start(n):
    count = 0
    b = []
    a = [66.25, 56, 89, 65, 34, 333, 333, 1, 1234.5]
    c = a[:n]
    print(a[n])
    x = n + 1
    b = [j for j in a[x:]]
#    print(b)
    for m in b:
        c.append(m)
    a = c
    print(a)

if __name__ == "__main__":
    import sys
    start(int(sys.argv[1]))

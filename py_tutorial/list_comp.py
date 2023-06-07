#!/usr/bin/pyhton3
count = 0
b = []
a = [66.25, 333, 333, 1, 1234.5]
for i in a:
    if i == 333:
        b = [j for j in a[count : ]]
        a = b
        print(a)
        break
    count += 1

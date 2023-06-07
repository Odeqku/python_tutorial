#!/usr/bin/python3
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	#print(f"{i}: {a[i]}", end=' ')
	print(f"{a[i]}", end=' ', flush=True)
print('\n')

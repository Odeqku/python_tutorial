#!/usr/bin/python3

# define the function as del (deletes content at any given idex n) 
def start(n):
    # declare and initializing list object b, and making it empty
    b = []
    a = [66.25, 333, 333, 1, 1234.5]
    # storing a slice (defined by the given index n) of a in c
    c = a[:n]
    x = n + 1
    """
    Iterating over the other half of a but with an ommision of...
    a[n], and storing the result of the operation in b 
    """
    b = [j for j in a[x:]]

    for m in b:
        c.append(m)
    a = c
    print(a)

if __name__ == "__main__":
    import sys
    start(int(sys.argv[1]))

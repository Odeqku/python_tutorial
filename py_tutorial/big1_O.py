#!/usr/bin/python3

def sarch(lis, low, high, target):
    while low <= high:
        mid = low + (high - low)//2
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    lis = [2, 4, 6, 8, 10, 12, 56]
    target = 10
    n = sarch(lis, 0, 6, target)
    print(n)

main()

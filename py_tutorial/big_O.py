#!/usr/bin/python3


def Towers(size, fromStack, toStack, spareStack):
    if size == 1:
        print('Move disk from {}, to, {}'.format(fromStack, toStack))
    else:
        print('Caught up size {}'.format(size))
        Towers(size-1, fromStack, spareStack, toStack)
        print('Here now')
        Towers(1, fromStack, toStack, spareStack)
        Towers(size-1, spareStack, toStack, fromStack)

def main():
    size = 3
    Towers(size, 'fromStack', 'toStack', 'spareStack')

main()

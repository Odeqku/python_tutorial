#!/usr/bin/python3

def make_matrix(rows, columns):
    '''
        >>> make_matrix(3, 5)
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        >>> make_matrix(4, 2)
        [[0, 0], [0, 0], [0, 0], [0, 0]]
    '''
    return [[0] * columns] * rows

if __name__ == '__main__':
    import doctest
    doctest.testmod()

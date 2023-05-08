#!/usr/bin/python3
""" Pascal's Triangle """

def  pascal_triangle(n):
    """ Returns a list of lists of integers representing 
        the Pascal's triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(0, i - 1):
            value = triangle[i - 1][j] + triangle[i - 1][j + 1]
            row.append(value)
        row.append(1)
        triangle.append(row)
    return triangle

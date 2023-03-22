import numpy as py
import sys as check
# print(slice_me(family, -1, -2))
# print(slice_me(family, 10, -2))
# print(slice_me([[12]], 0, 2))


def parsing_slice(family, start, end):
    '''parsing for slice'''
    if type(family) != list:
        print("Error: object provided is not a list 🤓")
        check.exit()
    for i in range(len(family)):
        if type(family[i]) != list:
            print("Error: List contains a non-list object 🤓")
            check.exit()
        for j in range(len(family[i])):
            if not isinstance(family[i][j], (int, float)):
                print("Error: list value is not an integer or a float 🤓")
                check.exit()
    for i in range(len(family)):
        for j in range(i+1, len(family)):
            if len(family[i]) != len(family[j]):
                print("Error: lists don't have the same size 🤓")
                check.exit()
    if type(start) != int:
        print("Error: start is not an int 🤓")
        check.exit()
    if type(end) != int:
        print("Error: end is not an int 🤓")
        check.exit()


def slice_me(family: list, start: int, end: int) -> list:
    '''slice an array'''
    parsing_slice(family, start, end)
    height = len(family)
    width = len(family[0])
    py_array = py.array(family)
    sliced_array = py_array[start:end, :]
    print("My shape is :", (height, width))
    height = len(sliced_array)
    width = len(sliced_array[0])
    print("My new shape is :", (height, width))
    return sliced_array.tolist()

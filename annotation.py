import numpy as np


data = [np.random.standard_normal() for i in range(7)]


def append_element(some_list,element):
    """
    Append element to the end of the list
    :param some_list: list
    :param element: element to be appended
    :return: None
    """
    some_list.append(element)

def isiterable(obj):
    """
    Check if the object is iterable
    :param obj: object
    :return: bool
    """
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
    

def addition():

    total = 0

    # 
    for i in range(100_000): # 
        # % is the modulo operator
        if i % 3  == 0 or i % 5 ==0:
            total += i


def apply_to_list(some_list,f):
    """
    Apply the function to each element of the list
    :param some_list: list
    :param f: function
    :return: list
    """
    return [f(x) for x in some_list]
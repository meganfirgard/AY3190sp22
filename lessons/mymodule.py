import numpy as np

def only_evens(list_of_numbers):
    """Take a list of numbers, and return a list of only the even numbers."""
    even_numbers = []
    for number in list_of_numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def only_evens_numpy(list_of_numbers):
    """Take a list of numbers, and return a list of only the even numbers using numpy."""
    number_array = np.array(list_of_numbers)
    evens = number_array % 2 == 0
    even_number_array = number_array[evens]
    return even_number_array
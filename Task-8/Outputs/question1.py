import numpy as np

def zeroInsert(first_term, last_term, elements, zeroes):

    user_arr = np.linspace(first_term, last_term, elements)       # Creating an array with the given first and term
    return_arr = np.zeros(len(user_arr)+(len(user_arr)-1)*zeroes) # Creating a zero array with size equal to (size of user_arr + zeroes)
    return_arr[::no_of_zeroes+1] = user_arr               # replacing the terms in the interval (no_of_zeroes +1)

    return return_arr


f_term = int(input("Enter the first of the array - "))
l_term = int(input("Enter the last of the array - "))
no_of_elements = int(input("How many numbers to be found (inclusive) - "))
no_of_zeroes = int(input("Enter the number of zeroes  - "))

print(zeroInsert(f_term, l_term, no_of_elements, no_of_zeroes))

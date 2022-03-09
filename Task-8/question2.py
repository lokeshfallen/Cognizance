import numpy as np
arr_1 =[]
arr_2 =[]

def equalCheck(arr_size):                       # Defining a function check whether the array are equal

    print("Enter the elements of first array - : ")
    for i in range(size):
        arr_1.append(int(input('Element - ')))

    print("Enter the elements of second array - ")
    for i in range(size):
        arr_2.append(int(input('Element - ')))

    result = np.all(arr_1 == arr_2)      # Calling all() function to check whether the arrays are equal.
    print(arr_1)
    print(arr_2)

    return result                        # returning the boolean value


size = int(input("ENTER THE SIZE OF ARRAYS - "))
print(equalCheck(size))            # Calling the function equalCheck()


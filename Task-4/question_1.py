# Program to find the sum of two numbers obtained from the user.

def add(num1, num2):
    sum = (num1) + (num2)
    return sum


num_1 = int(input("Enter the first number - "))
num_2 = int(input("Enter the second number - "))
print(f' Sum = {add(num_1, num_2)}')
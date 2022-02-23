# Program to find whether a given number is a palindrome.

def palindrome(number):

    rev_num = 0
    temp_num = number
    count = 0
    while temp_num != 0:                 # Loop to find the no.of.digits
        temp_num = int(temp_num / 10)
        count += 1
    i = count - 1
    while number != 0:                     # Loop to reverse the number
        rev_num += (number % 10)*(10**i)
        number = int (number / 10)
        i -= 1

    return rev_num


num = int(input("Enter the number to be checked - "))
if num == palindrome(num):
    print("IT IS A PALINDROME")
else:
    print("IT IS NOT A PALINDROME")

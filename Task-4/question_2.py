# PrograLm to get a string from the user and display only the character in even index positions.
# Method-1

def evenDisp(str, strlen):
    string_1 = ''

    for i in range(int(strlen)):
        if i % 2 == 0:
            string_1 += str[i]

    return string_1


string = input("Enter the string - ")
print(f'Result -- {evenDisp(string, len(string))}')
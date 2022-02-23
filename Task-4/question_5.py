# Program to print * pyramid with 5 rows.

def pyramid():
    for i in range(1,6):
        gaps = 5 - i
        for j in range(gaps):              # Loop to print the gaps
            print(end=" ")
        for j in range(0,i):               # Loop to print '*'
            print("*", end= " ")

        print('\r')

pyramid()
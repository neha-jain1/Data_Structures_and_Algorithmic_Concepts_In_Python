#The aim of this program that reads values from the user until a blank line is entered. Display
#the total of all of the values entered by the user (or 0.0 if the first value entered is
#a blank line).


def sum_input():
    n = input()
    if(n==''):
        return 0
    return (int(n) + sum_input())


print(sum_input())
    

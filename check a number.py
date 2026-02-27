""" Print & Input (Very Basic)

Write a Python program that:

Takes a number from the user

Prints “Positive” if the number is greater than 0 """


num = int(input("Enter a number : "))

if num > 0 :
    print(num , "is positive")
elif num < 0 :
    print(num , "is negative")
else :
    print("It is" , num)
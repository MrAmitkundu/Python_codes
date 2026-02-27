"""Greater Number (if–else)

Write a Python program that:

Takes two numbers as input

Prints which number is greater

If both are equal, print “Both are equal”"""

num_1 = int(input("Enter the 1st number : "))
num_2 = int(input("Enter the 2nd number : "))

if num_1 > num_2 :
    print("1st number (" ,num_1,")" , "is greater than 2nd number (" , num_2,")")
elif num_2 > num_1 :
    print("2nd number (" ,num_2,")" , "is greater than 1st number (" , num_1,")")
else :
    print(num_1 ,"&" , num_2 , "both are equal")




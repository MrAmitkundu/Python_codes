"""Pass or Fail (if–elif–else)

Write a Python program that:

Takes marks as input

If marks ≥ 40 → print “Pass”

If marks < 40 → print “Fail”"""

name = input("Enter your name : ")
marks = int(input("Enter your total marks : "))

if marks >= 40 :
    print(name , ", you pass the examination ")
else :
    print(name , ", you fail in the examination")





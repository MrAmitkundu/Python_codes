"""The program should:

Ask the user for an input, which represents their current experience level in Spanish. If the student has not taken any
Spanish classes, he can enter “none” otherwise he can enter the class number.
If a student has no experience, the program should recommend taking 101.
If a student has taken one of the first three course, it should recommend the next course in the sequence.
If the student has already taken 202, then the program should recommend that the student move on to advanced courses.
I recommend that you attempt to write this program on your own first. After you finish, or get as close as you can,
 you can come back here to compare your solution to mine. You can click on the button below to reveal the answer
  (or really, one of many possible answers!)."""

name = input("Enter your name : ")
print("Enter your current experience level in Spanish ")
print("between this options (101 / 102 / 201 / 202 / none)")

experience = input(">>> ")

if experience == "none" :
    print(name ,"Please take our Spanish 101 course ")
elif experience == "101" :
    print(name , "Please take our Spanish 102 course ")
elif experience == "102" :
    print(name, "Please take our Spanish 201 course ")
elif experience == "201" :
    print(name ,"Please take our Spanish 202 course ")
elif experience == "202" :
    print(name ,"Please take advance courses ")
else :
    print(name ,"Please enter your experience correctly ")










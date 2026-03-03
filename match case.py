
try:
    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Invalid Choice")

except ValueError:
    print("Please enter a valid number!")



# choice = int(input("Enter your choice : "))
#
# match choice :
#     case 1 :
#         print("Sunday ")
#     case 2:
#         print("Monday ")
#     case 3:
#         print("Tuesday ")
#     case 4:
#         print("Wednesday ")
#     case 5:
#         print("Thursday ")
#     case 6:
#         print("Friday ")
#     case 7:
#         print("Saturday ")
#     case _:
#         print("Invalid Choice ")

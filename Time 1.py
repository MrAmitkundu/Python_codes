import time

local_Time = time.localtime()

a_Time = time.strftime("%H:%M:%S" , local_Time)

current_hour = int(time.strftime("%H",local_Time))


if 6 <= current_hour < 12:
    print("Good Morning Sir")
elif 12 <= current_hour < 17:
    print("Good Afternoon Sir")
elif 17 <= current_hour < 20:
    print("Good Evening Sir")
else:
    print("Good Night Sir")
    # if Hour <= 24 :
    #     print("Good Night Sir ")
    # else :
    #     print("Your Current time is invalid")


# if Hour >= 6 and Hour < 12:
#     print("Good Morning Sir ")
# elif Hour >= 12 and Hour < 17 :
#     print("Good Afternoon Sir ")
# elif Hour >= 17 and Hour <= 19:
#     print("Good Evening Sir ")
# elif Hour >= 24 and Hour <= 0 :
#     print("Your Current time is invalid")
# else :
#     print("Good Night Sir")
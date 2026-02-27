width = int(input("enter the width of the pattern : "))
height = int(input("enter the height of the pattern : "))

width_of_third = int(width / 3)
half_of_height = int(height / 2)



upperrows = '-' * width_of_third + '#' * width_of_third + '-' * width_of_third + '\n'
lowerrows = '#' * width_of_third + '-' * width_of_third + '#' * width_of_third + '\n'

print(upperrows * half_of_height , end='')
print(lowerrows * half_of_height , end='')





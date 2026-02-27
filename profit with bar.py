revenue = int(input("Enter the bussiness revenue : "))
cost = int(input("Enter the bussiness cost : "))

profit = revenue - cost

print("Profit of the bussines is : ",profit)

print("Bar graphs :")

revenue_bar = '#' * 50
cost_bar = '#' * int(((cost / revenue ) *50))
profit_bar = '#' * int(((profit / revenue) *50))

print("Revenue : ", revenue_bar)
print("Cost    : ", cost_bar)
print("Profit  : ", profit_bar)

amount = int(input("Enter any number or no money"))

rupee100 = amount // 100
rupee50 = (amount%100) // 50
rupee10= ((amount%100)%50) //10

print("Number of 100 rupee notes -", rupee100)
print("Number of 50 rupee notes -", rupee50)
print("Number of 10 rupee notes -", rupee10)


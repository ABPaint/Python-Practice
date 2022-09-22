print("Enter your numbers")
num1 = input("First:")
num2 = input("Second:")
num3 = input("Third:")




if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print(largest)
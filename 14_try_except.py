num1 = (input("Enter num1: "))
num2 = (input("Enter num2: "))
try:
    print("The sum of these two numbers is", int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")
x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

z = int(input("Choose your operation: \n 1.Addition \n 2. Substraction \n 3.Multiplication \n 4.Division \n Enter your operation number:"))

if (z == 1):
    print(x+y)

elif (z == 2):
    print(x-y)

elif (z == 3):
    print(x*y)

elif (z == 4):
    print(x/y)

else:
    print("Enter an appropriate operation")
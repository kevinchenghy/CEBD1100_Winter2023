number = input("Enter a number to test:")

# if number.isnumeric():

if int(number) % 10 == 0 and int(number) < 100:
    print("Yes, the number is less than 100 and a multiple of 10")
else:
    print("No, the number is not less than 100 and a multiple of 10")
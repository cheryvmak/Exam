

# Q1

#  A Basic Calculator

# (+, -, *, /)


# addition function
def add(a, b):
    return a + b 

# subtraction function
def subtract(a, b):
    return a - b

#multiplication function
def multiply(a, b):
    return a * b

# Division function
def divide(a, b):
    if b != 0:
        return a / b

# The user interface
print("--" * 15)
print("A Basic calculator")
print("--" * 15)
print("Select operation to perform from the Menu: ")
print("\n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True: 
    try:
        choice = input("Enter your choice :")

        if choice == "1":
            num_1 = int(input("Enter the first number:"))
            num_2 = int(input("Enter the second number:"))
            print("Result: ", add(num_1, num_2))


        elif choice == "2":
            num_1 = int(input("Enter the first number:"))
            num_2 = int(input("Enter the second number:"))
            print("Result: ", subtract(num_1, num_2))
        

        elif choice == "3":
            num_1 = int(input("Enter the first number:"))
            num_2 = int(input("Enter the second number:"))
            print("Result: ", multiply(num_1, num_2))
        

        elif choice == "4":
            num_1 = int(input("Enter the first number:"))
            num_2 = int(input("Enter the second number:"))
            print("Result: ", divide(num_1, num_2))

        elif choice == "5":
            print("You exit from the program")
            break

        else:
            print("Invalid Entry!")
    except ValueError:
        print(" Please check. this is value error")
            

# Q2


while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break       # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")



# Q3
while True:
    age = int(input("Enter your age (or type exit to quit): "))
    if age == exit:
        print("Goodbye!")
        break

    try:
        if age >= 18:
                print("You can vote")
        else:
                print("You cannot vote")
    except:
            print("Invalid input")
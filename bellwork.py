
# Part 1
# Evaluating given expressions
expr1 = 5 + 3 * 2
expr2 = (10 - 4) / 2
expr3 = 7 % 3
expr4 = 2 ** 3 + 1

# Printing the results
print("5 + 3 * 2 =", expr1)
print("(10 - 4) / 2 =", expr2)
print("7 % 3 =", expr3)
print("2 ** 3 + 1 =", expr4)

# Part 1b
def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by both 3 and 5.")
    else:
        print(f"{num} is not divisible by both 3 and 5.")

# Part2
def square_and_cube(num):
    return (num ** 2, num ** 3)
# Part2b
def greet_user(name):
    return "Hello, " + name + "!"

# part3
for num in range(2, 21, 2):
    print(num, end=", ")

# part3b
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        break  # Exit the loop
    
    if user_input.isdigit():  # Check if input is a number
        num = int(user_input)
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    else:
        print("Invalid input. Please enter a number or 'exit'.")




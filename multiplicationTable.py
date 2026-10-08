
# Homework 2: Multiplication Table

number = int(input("Enter your number: "))

print(f"\n===== Multiplication Table of {number} =====")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

print("==========================")

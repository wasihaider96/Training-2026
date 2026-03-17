#Take input from user
num = int(input("Enter a number (1-12): "))

#Validate Input using while loop
while num < 1 or num > 12:
    print("invalid input! Please try again.")
    num = int(input("Enter a number (1-12): "))

# Print Multiplication table
print(f"\nMultiplication Table for {num}:\n")

for i in range(1, 13):
    result = num * i
    print(f"{num:2} x {i:2} = {result:3}")

#Bonus: Print all tables from 1 to 12
print("\n\nAll Tables from 1 to 12:\n")

for n in range(1, 13):
    print(f"\nTable of {n}")
    print("-" * 20)

    for i in range(1,13):
        result = n * i
        print(f"{n:2} x {i:2} = {result:3}")
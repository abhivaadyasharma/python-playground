# Step 1: Ask the user how many numbers they want to add
while True:
 num_count = int(input("How many numbers would you like to add? "))

# Initialize a variable to store the sum
 total_sum = 0

# Step 2: Ask the user for the numbers one by one
 for i in range(1, num_count + 1):
    number = float(input(f"Enter number {i}: "))
    total_sum += number

# Step 3: Print the sum
 print(f"The sum of the numbers is: {total_sum}")

 #Ask if the user wants to make another calculation
 repeat = input("\nDo you want to calculate sumno? (yes/no): ").lower()
 if repeat != "yes":
            print("Thank you for using the calculator! Goodbye.")
            break  # Exits the while loop

def multiply_numbers(n):
    if n < 1:  # Check if the input is valid
        return "Please enter a number greater than or equal to 1."

    result = 1
    i = n  # Start at the given number
    while i > 0:  # Loop until i is 0
        result *= i
        i -= 1  # Decrement i to go to the next number
    return result

# Main loop
while True:
    number = int(input("Enter a number: "))
    print(f"The result is: {multiply_numbers(number)}")

    # Ask the user if they want to perform the operation again
    again = input("Do you want to perform the operation again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

while True:
    num = int(input("Enter a number (or type 'exit' to quit): "))
    
    # Check if the number is even or odd
    print(f"The number {num} is {check_even_odd(num)}.")
    
    # Ask the user if they want to continue or exit
    continue_choice = input("Do you want to check another number? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Goodbye!")
        break

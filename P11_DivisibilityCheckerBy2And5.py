def check_divisibility(number):
    """Check divisibility and print appropriate message."""
    if number % 2 == 0 and number % 5 == 0:
        print(f"\n{number} is divisible by both 2 and 5.")
    elif number % 2 == 0:
        print(f"\n{number} is divisible by 2 but not by 5.")
    elif number % 5 == 0:
        print(f"\n{number} is divisible by 5 but not by 2.")
    else:
        print(f"\n{number} is not divisible by either 2 or 5.")

while True:
    # Ask the user for a number or exit
    user_input = input("\nEnter a number to check divisibility (or type 'exit' to quit): ").lower()

    # Exit if the user types 'exit'
    if user_input == 'exit':
        print("\nGoodbye! Thanks for using the program.")
        break

    try:
        # Try converting the input to a float
        number = float(user_input)

        # Call the function to check divisibility
        check_divisibility(number)

    except ValueError:
        print("\nInvalid input! Please enter a valid number or 'exit' to quit.")

    # Ask if the user wants to check another number
    continue_choice = input("\nDo you want to check another number? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("\nGoodbye! Thanks for using the program.")
        break


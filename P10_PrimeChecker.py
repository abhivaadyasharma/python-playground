def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

while True:
    num = int(input("Enter a number (or type 'exit' to quit): "))
    
    # Check if the number is prime
    if check_prime(num):
        print(f"The number {num} is prime.")
    else:
        print(f"The number {num} is not prime.")
    
    # Ask the user if they want to continue or exit
    continue_choice = input("Do you want to check another number? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Goodbye!")
        break

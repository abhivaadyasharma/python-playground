# Author: Abhivaadya Sharma

def square():
    while True:
        try:
            sidesq = float(input("Side of square: "))
            if sidesq <= 0:
                print("Side length must be a positive number. Please try again.")
                continue
            areasq = sidesq * sidesq
            print(f"Area of the square: {areasq:.2f}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def rectangle():
    while True:
        try:
            length = float(input("What is the length? "))
            breadth = float(input("What is the breadth? "))
            if length <= 0 or breadth <= 0:
                print("Length and breadth must be positive numbers. Please try again.")
                continue
            area_of_rectangle = length * breadth
            print(f"Area of rectangle: {area_of_rectangle:.2f}")
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def triangle():
    while True:
        try:
            height = float(input("Height: "))
            base = float(input("Base: "))
            if height <= 0 or base <= 0:
                print("Height and base must be positive numbers. Please try again.")
                continue
            area_of_triangle = 0.5 * height * base
            print(f"Area of triangle: {area_of_triangle:.2f}")
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def circle():
    while True:
        try:
            radius = float(input("Radius: "))
            if radius <= 0:
                print("Radius must be a positive number. Please try again.")
                continue
            area_of_circle = 3.14159265359 * radius * radius
            print(f"Area of circle: {area_of_circle:.2f}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        print("\nAvailable shapes: [square, rectangle, triangle, circle]")
        choice = input("Out of the above options, which shape's area do you want to calculate? ").lower()

        if choice == "square":
            square()
        elif choice == "rectangle":
            rectangle()
        elif choice == "triangle":
            triangle()
        elif choice == "circle":
            circle()
        else:
            print("Invalid choice. Please enter a valid option.")

        # Ask if the user wants to make another calculation
        repeat = input("\nDo you want to calculate another area? (yes/no): ").lower()
        if repeat != "yes":
            print("Thank you for using the area calculator! Goodbye.")
            break  # Exits the while loop

if __name__ == "__main__":
    main()

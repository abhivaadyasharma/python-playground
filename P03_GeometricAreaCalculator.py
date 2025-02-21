#Author: Abhivaadya Sharma

def square():
    sidesq = float(input("Side of square: "))
    areasq = sidesq * sidesq
    print("Area of the square: ", areasq)


def rectangle():
    length = float(input("What is length? "))
    breadth = float(input("What is breadth? "))
    area_of_rectangle = length * breadth
    print("Area of rectangle:", area_of_rectangle)


def triangle():
    height = float(input("Height: "))
    base = float(input("Base: "))
    area_of_triangle = 0.5 * height * base
    print("Area of triangle:", area_of_triangle)


def circle():
    radius = float(input("Radius: "))
    area_of_circle = 3.14159265359 * radius * radius
    print("Area of circle:", area_of_circle)

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
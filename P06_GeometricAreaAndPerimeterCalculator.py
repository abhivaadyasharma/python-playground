#Author: Abhivaadya Sharma

def area():
    print("Available shapes: [square, rectangle, triangle, circle]")
    choice = input("Out of the above options, which shape's area do you want to calculate? ").lower()

    if choice == "square":
        square_area()

    elif choice == "rectangle":
        rectangle_area()

    elif choice == "triangle":
        triangle_area()

    elif choice == "circle":
        circle_area()

    else:
        print("Invalid choice. Please enter a valid option.")

def square_area():
    sidesq = float(input("Side of square: "))
    areasq = sidesq * sidesq
    print("Area of the square: ", areasq)

def rectangle_area():
    length = float(input("What is length? "))
    breadth = float(input("What is breadth? "))
    area_of_rectangle = length * breadth
    print("Area of rectangle:", area_of_rectangle)

def triangle_area():
    height = float(input("Height: "))
    base = float(input("Base: "))
    area_of_triangle = 0.5 * height * base
    print("Area of triangle:", area_of_triangle)

def circle_area():
    radius = float(input("Radius: "))
    area_of_circle = 3.14159265359 * radius * radius
    print("Area of circle:", area_of_circle)

def perimeter():
    print("Available shapes: [square, rectangle, triangle, circle]")
    choice = input("Out of the above options, which shape's perimeter do you want to calculate? ").lower()

    if choice == "square":
        square_perimeter()

    elif choice == "rectangle":
        rectangle_perimeter()

    elif choice == "triangle":
        triangle_perimeter()

    elif choice == "circle":
        circle_perimeter()

    else:
        print("Invalid choice. Please enter a valid option.")

def square_perimeter():
    side = float(input("What is the length of side? "))
    perimeter_of_square = 4 * side
    print("Perimeter of square:", perimeter_of_square)

def rectangle_perimeter():
    length = float(input("What is length of rectangle? "))
    breadth = float(input("What is breadth of rectangle? "))
    perimeter_of_rectangle = 2 * (length + breadth)
    print("Perimeter of rectangle:", perimeter_of_rectangle)

def triangle_perimeter():
    number_1 = float(input("What is length of First side? ")) 
    number_2 = float(input("What is length of Second side? ")) 
    number_3 = float(input("What is length of Third side? ")) 
    perimeter_of_triangle = number_1 + number_2 + number_3
    print("Perimeter of triangle:", perimeter_of_triangle)

def circle_perimeter():
    radius = float(input("What is length of radius? ")) 
    perimeter_of_circle = 2 * 3.14159265359  * radius
    print("Perimeter of circle:", perimeter_of_circle)

def main():
    while True:
        print("\nAvailable calculations: [perimeter, area]")
        choice = input("Out of the above options, which calculation do you want to perform? ").lower()

        if choice == "perimeter":
            perimeter()
        elif choice == "area":
            area()

        else:
            print("Invalid choice. Please enter a valid option.")

        # Ask if the user wants to make another calculation
        repeat = input("\nDo you want to calculate another area or perimeter? (yes/no): ").lower()
        if repeat != "yes":
            print("Thank you for using the calculator! Goodbye.")
            break  # Exits the while loop

if __name__ == "__main__":
    main()   
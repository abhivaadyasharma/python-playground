#Author: Abhivaadya Sharma

def square():
    side=float(input("What is the length of side? "))
    Perimeter_of_square=4*side
    print ("Perimeter of square:",Perimeter_of_square)

def rectangle():
    length=float(input("What is length of rectangle? "))
    breadth=float(input("What is breadth of rectangle? "))
    Perimeter_of_rectangle=2*(length+breadth)
    print ("Perimeter of rectangle:", Perimeter_of_rectangle)


def triangle():
    number_1= float(input("What is length of First side? ")) 
    number_2=float(input("What is length of Second side? ")) 
    number_3=float(input("What is length of Third side? ")) 
    Perimeter_of_triangle=number_1+number_2+number_3
    print ("Perimeter of triangle:", Perimeter_of_triangle)


def circle():
    radius=float(input("What is length of radius? ")) 
    Perimeter_of_circle= 2*3.14159265359*radius
    print ("Perimeter of circle:", Perimeter_of_circle)


def main():
    while True:  
        print("Available shapes: [square, rectangle, triangle, circle]")
        choice = input("Out of the above options, which shape's perimeter do you want to calculate? ").lower()

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

        repeat = input("Do you want to calculate another areperimtera? (yes/no): ").lower()
        if repeat != "yes":
            print("Thank you for using the area calculator! Goodbye.")
            break   

if __name__ == "__main__":
    main()
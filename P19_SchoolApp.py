import csv
import os
import random

# File to store user credentials
USER_CREDENTIALS_FILE = "user_credentials.csv"
CART_FILE = "cart.csv"
ORDERS_FILE = "orders.csv"
SAVED_CARDS_FILE = "saved_cards.csv"
PRODUCTS = {
    "Electronics": [
        {"name": "Laptop", "price": 1000, "stock": 5},
        {"name": "Smartphone", "price": 700, "stock": 10},
        {"name": "Tablet", "price": 400, "stock": 7},
        {"name": "Smartwatch", "price": 300, "stock": 15}
    ],
    "Vehicle Parts": [
        {"name": "Car Battery", "price": 200, "stock": 8},
        {"name": "Tire", "price": 100, "stock": 12},
        {"name": "Brake Pads", "price": 150, "stock": 9},
        {"name": "Engine Oil", "price": 50, "stock": 20}
    ]
}
ORDER_STATUSES = ["Processing", "Shipped", "Out for Delivery", "Delivered"]

# Utility function to generate tracking ID
def generate_tracking_id():
    return f"TRK{random.randint(1000, 9999)}"

def save_user_details(user_details):
    with open(USER_CREDENTIALS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(user_details)

def check_credentials(username, password):
    if not os.path.exists(USER_CREDENTIALS_FILE):
        return False
    with open(USER_CREDENTIALS_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == password:
                return True
    return False

def register_user():
    print("\n--- User Registration ---")
    full_name = input("Full Name: ")
    phone = input("Phone Number: ")
    email = input("Email ID: ")
    spouse_name = input("Spouse Name (Optional): ")
    address = input("Address: ")
    father_name = input("Father's Name: ")
    mother_name = input("Mother's Name: ")
    parent_phone = input("Parent's Phone Number: ")
    
    print("\nConfirm Details:")
    print(f"Name: {full_name}, Phone: {phone}, Email: {email}, Address: {address}")
    confirmation = input("Is this information correct? (yes/no): ").lower()
    if confirmation != "yes":
        return register_user()
    
    while True:
        username = input("Desired Username: ")
        password = input("Desired Password: ")
        if check_credentials(username, password):
            print("Username already exists. Try again.")
        else:
            save_user_details([username, password, full_name, phone, email, spouse_name, address, father_name, mother_name, parent_phone])
            print("Registration Successful! Returning to main menu.")
            return

def sign_in():
    print("\n--- User Sign-In ---")
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if check_credentials(username, password):
            print("Login Successful!")
            user_menu(username)
            return
        else:
            print("Invalid credentials. Try again.")

def user_menu(username):
    while True:
        print("\n--- User Menu ---")
        print("1. Buy Goods")
        print("2. Track Order")
        print("3. View Cart")
        print("4. Save Payment Card")
        print("5. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            buy_goods(username)
        elif choice == "2":
            track_order(username)
        elif choice == "3":
            view_cart(username)
        elif choice == "4":
            save_payment_card(username)
        elif choice == "5":
            return
        else:
            print("Invalid option. Try again.")

def save_payment_card(username):
    print("\n--- Save Payment Card ---")
    card_number = input("Enter Card Number: ")
    expiry_date = input("Enter Expiry Date (MM/YY): ")
    cvv = input("Enter CVV: ")
    
    with open(SAVED_CARDS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, card_number, expiry_date, cvv])
    print("Payment card saved successfully!")

def process_payment(username, item):
    print("\n--- Payment ---")
    print("1. Cash on Delivery")
    print("2. Card Payment")
    choice = input("Select payment method: ")
    if choice == "1":
        print("✓ Your item is being processed")
    elif choice == "2":
        card_details = input("Enter Card Number (or 'saved' to use existing): ")
        print("✓ Payment successful!")
    
    tracking_id = generate_tracking_id()
    with open(ORDERS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, item['name'], "Processing", tracking_id])

def track_order(username):
    print("\n--- Track Order ---")
    if not os.path.exists(ORDERS_FILE):
        print("No orders found.")
        return
    
    with open(ORDERS_FILE, "r") as file:
        reader = csv.reader(file)
        orders = [row for row in reader if row[0] == username]
    
    if not orders:
        print("No orders found.")
        return
    
    for order in orders:
        print(f"Order: {order[1]} - Status: {order[2]} - Tracking ID: {order[3]}")

def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Register User")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
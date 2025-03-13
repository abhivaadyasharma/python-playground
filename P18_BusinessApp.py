class SalesMan:
    def __init__(self, username, password, stock):
        self.username = username
        self.password = password
        self.stock = stock  # Stock is a dictionary of items and their quantities

    def login(self, username, password):
        """Authenticate user login."""
        if self.username == username and self.password == password:
            return True
        return False

    def view_items(self):
        """View available items for sale."""
        print("Items available for sale:")
        for item, qty in self.stock.items():
            print(f"{item}: {qty} in stock")
    
    def sell_item(self, item, qty_sold):
        """Sell an item if enough stock is available."""
        if item in self.stock and self.stock[item] >= qty_sold:
            self.stock[item] -= qty_sold
            print(f"Sold {qty_sold} {item}. Remaining stock: {self.stock[item]}")
            return True
        print("Not enough stock!")
        return False

    def receive_salary(self, salary):
        """Receive salary after sales."""
        print(f"{self.username} received salary: {salary} Rs")

    def receive_notification(self, message):
        """Receive notifications (for sales, updates, etc.)."""
        print(f"Notification for {self.username}: {message}")


class SalesPersonManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sales_men = []  # List of SalesMan objects
        self.items = []  # Items in stock to add/manage

    def login(self, username, password):
        """Authenticate manager login."""
        if self.username == username and self.password == password:
            return True
        return False

    def add_item(self, item_name, qty):
        """Add items to stock."""
        self.items.append({'item_name': item_name, 'quantity': qty})
        print(f"Added item: {item_name} with {qty} units.")

    def view_sales(self):
        """View sales report for each salesman."""
        print("Sales report:")
        for salesman in self.sales_men:
            total_sales = sum(salesman.stock.values())  # Total items sold
            print(f"{salesman.username}: Sold {total_sales} items.")
    
    def pay_salary(self):
        """Calculate and pay salaries to all salesmen based on sales."""
        for salesman in self.sales_men:
            total_sales = sum(salesman.stock.values())  # Total items sold
            salary = total_sales * 1000  # 1000 Rs per item sold
            salesman.receive_salary(salary)
            print(f"Paid {salesman.username} {salary} Rs for {total_sales} items sold.")

    def hire_salesman(self, name, username, password):
        """Hire a new salesman."""
        salesman = SalesMan(username, password, {})
        self.sales_men.append(salesman)
        print(f"Hired {name} as a salesman.")
    
    def fire_salesman(self, username):
        """Fire an existing salesman."""
        for salesman in self.sales_men:
            if salesman.username == username:
                self.sales_men.remove(salesman)
                print(f"Fired salesman {username}.")
                return
        print("Salesman not found.")

    def send_notification_to_salesmen(self, message):
        """Send notifications to all salesmen."""
        for salesman in self.sales_men:
            salesman.receive_notification(message)


class DevelopmentTeam:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        """Authenticate developer login."""
        if self.username == username and self.password == password:
            return True
        return False

    def send_code(self):
        """Send code updates to the manager."""
        print("Sending code to manager...")
        print("Code sent.")


class CEO:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sales_managers = []  # List of SalesPersonManager objects
        self.development_team = []  # List of DevelopmentTeam objects

    def login(self, username, password):
        """Authenticate CEO login."""
        if self.username == username and self.password == password:
            return True
        return False

    def hire_sales_manager(self, name, username, password):
        """Hire a new Sales Manager."""
        manager = SalesPersonManager(username, password)
        self.sales_managers.append(manager)
        print(f"Hired {name} as Sales Manager.")
    
    def fire_sales_manager(self, username):
        """Fire an existing Sales Manager."""
        for manager in self.sales_managers:
            if manager.username == username:
                self.sales_managers.remove(manager)
                print(f"Fired Sales Manager {username}.")
                return
        print("Sales Manager not found.")
    
    def hire_development_team(self, name, username, password):
        """Hire a new member for the Development Team."""
        dev = DevelopmentTeam(username, password)
        self.development_team.append(dev)
        print(f"Hired {name} as Development Team member.")
    
    def fire_development_team(self, username):
        """Fire an existing member of the Development Team."""
        for dev in self.development_team:
            if dev.username == username:
                self.development_team.remove(dev)
                print(f"Fired Development Team member {username}.")
                return
        print("Development Team member not found.")


def main():
    # Initialize app data
    ceo = CEO("ceo_username", "ceo_password")
    manager = SalesPersonManager("manager_username", "manager_password")
    developer = DevelopmentTeam("dev_username", "dev_password")
    
    # Assign manager and developer to CEO
    ceo.sales_managers.append(manager)
    ceo.development_team.append(developer)

    # Sample SalesMan creation by Manager
    salesman = SalesMan("salesman_username", "salesman_password", {'item1': 100, 'item2': 50})
    manager.sales_men.append(salesman)

    # User input loop
    while True:
        print("Login as:\n1. SalesMan\n2. Sales Person Manager\n3. Development Team\n4. CEO\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            for salesman in manager.sales_men:
                if salesman.login(username, password):
                    print("Logged in as SalesMan.")
                    salesman.view_items()
                    item = input("Enter item to sell: ")
                    qty = int(input("Enter quantity to sell: "))
                    salesman.sell_item(item, qty)
                    break
            else:
                print("Invalid login!")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if manager.login(username, password):
                print("Logged in as Sales Manager.")
                action = input("1. Add Item\n2. View Sales\n3. Pay Salary\n4. Hire SalesMan\n5. Fire SalesMan\n6. Send Notification\n")
                if action == '1':
                    item_name = input("Enter item name: ")
                    qty = int(input("Enter quantity: "))
                    manager.add_item(item_name, qty)
                elif action == '2':
                    manager.view_sales()
                elif action == '3':
                    manager.pay_salary()
                elif action == '4':
                    name = input("Enter SalesMan name: ")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    manager.hire_salesman(name, username, password)
                elif action == '5':
                    username = input("Enter SalesMan username to fire: ")
                    manager.fire_salesman(username)
                elif action == '6':
                    message = input("Enter notification message: ")
                    manager.send_notification_to_salesmen(message)
            else:
                print("Invalid login!")

        elif choice == '3':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if developer.login(username, password):
                print("Logged in as Development Team.")
                developer.send_code()
            else:
                print("Invalid login!")

        elif choice == '4':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if ceo.login(username, password):
                print("Logged in as CEO.")
                action = input("1. Hire Sales Manager\n2. Fire Sales Manager\n3. Hire Development Team\n4. Fire Development Team\n")
                if action == '1':
                    name = input("Enter Sales Manager name: ")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    ceo.hire_sales_manager(name, username, password)
                elif action == '2':
                    username = input("Enter Sales Manager username to fire: ")
                    ceo.fire_sales_manager(username)
                elif action == '3':
                    name = input("Enter Development Team member name: ")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    ceo.hire_development_team(name, username, password)
                elif action == '4':
                    username = input("Enter Development Team username to fire: ")
                    ceo.fire_development_team(username)
            else:
                print("Invalid login!")

        elif choice == '5':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

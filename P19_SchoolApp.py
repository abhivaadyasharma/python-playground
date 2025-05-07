import csv
import os

# ==== FILE PATHS ====
STUDENT_FILE = "students.csv"
TEACHER_FILE = "teachers.csv"
NOTIFY_FILE = "notifications.csv"
MARKS_FILE = "marks.csv"

# ==== HELPERS ====
def ensure_files():
    for f, headers in [
        (STUDENT_FILE, ["username", "password", "name", "class", "section", "roll_no",
                        "father_name", "father_phone", "mother_name", "mother_phone", "email"]),
        (TEACHER_FILE, ["username", "password", "name", "email", "phone", "subject"]),
        (NOTIFY_FILE, ["to_student", "message"]),
        (MARKS_FILE, ["student", "exam", "marks"])
    ]:
        if not os.path.exists(f):
            with open(f, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)

def read_csv(filename):
    with open(filename, "r", newline="") as file:
        return list(csv.DictReader(file))

def write_csv(filename, rows, fieldnames):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def append_csv(filename, row):
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        if not file_exists or os.stat(filename).st_size == 0:
            writer.writeheader()
        writer.writerow(row)

# ==== CORE CLASSES ====
class Student:
    def __init__(self, username):
        self.username = username

    def get_info(self):
        for s in read_csv(STUDENT_FILE):
            if s["username"] == self.username:
                return s
        return {}

    def first_time_info(self):
        info = self.get_info()
        updated = {
            "username": self.username,
            "password": info["password"],
            "name": input("Name: "),
            "class": input("Class: "),
            "section": input("Section: "),
            "roll_no": input("Roll no.: "),
            "father_name": input("Father's Name: "),
            "father_phone": input("Father's Phone: "),
            "mother_name": input("Mother's Name: "),
            "mother_phone": input("Mother's Phone: "),
            "email": input("Email: ")
        }
        students = read_csv(STUDENT_FILE)
        for s in students:
            if s["username"] == self.username:
                s.update(updated)
        write_csv(STUDENT_FILE, students, students[0].keys())
        print("Info updated!")

    def update_info(self):
        info = self.get_info()
        for key in info:
            if key in ["username", "password"]:
                continue
            new_val = input(f"{key} (leave blank to keep '{info[key]}'): ")
            if new_val:
                info[key] = new_val
        students = read_csv(STUDENT_FILE)
        for s in students:
            if s["username"] == self.username:
                s.update(info)
        write_csv(STUDENT_FILE, students, students[0].keys())
        print("Info updated!")

    def view_notifications(self):
        notes = [n["message"] for n in read_csv(NOTIFY_FILE) if n["to_student"] == self.username]
        if not notes:
            print("No notifications.")
        else:
            for note in notes:
                print("->", note)

    def view_marks(self):
        exam = input("Exam (Unit-Test:1 / Unit-Test:2 / Mid-Term / Annual): ")
        found = False
        for m in read_csv(MARKS_FILE):
            if m["student"] == self.username and m["exam"] == exam:
                print(f"{exam} Marks: {m['marks']}")
                found = True
        if not found:
            print("No marks found for this exam.")

    def view_teachers(self):
        for t in read_csv(TEACHER_FILE):
            print(f"{t['name']} - Email: {t['email']} - Phone: {t['phone']}")

class Teacher:
    def __init__(self, username):
        self.username = username

    def get_info(self):
        for t in read_csv(TEACHER_FILE):
            if t["username"] == self.username:
                return t
        return {}

    def first_time_info(self):
        info = self.get_info()
        updated = {
            "username": self.username,
            "password": info["password"],
            "name": input("Name: "),
            "email": input("Email: "),
            "phone": input("Phone: "),
            "subject": input("Subject: ")
        }
        teachers = read_csv(TEACHER_FILE)
        for t in teachers:
            if t["username"] == self.username:
                t.update(updated)
        write_csv(TEACHER_FILE, teachers, teachers[0].keys())
        print("Info updated!")

    def update_info(self):
        info = self.get_info()
        for key in info:
            if key in ["username", "password"]:
                continue
            new_val = input(f"{key} (leave blank to keep '{info[key]}'): ")
            if new_val:
                info[key] = new_val
        teachers = read_csv(TEACHER_FILE)
        for t in teachers:
            if t["username"] == self.username:
                t.update(info)
        write_csv(TEACHER_FILE, teachers, teachers[0].keys())
        print("Info updated!")

    def send_notification(self):
        student = input("Enter student username: ")
        append_csv(NOTIFY_FILE, {"to_student": student, "message": input("Enter message: ")})
        print("Notification sent.")

    def add_marks(self):
        student = input("Enter student username: ")
        exam = input("Exam: ")
        marks = input("Marks: ")
        append_csv(MARKS_FILE, {"student": student, "exam": exam, "marks": marks})
        print("Marks recorded.")

    def view_students_info(self):
        for s in read_csv(STUDENT_FILE):
            print(f"{s['name']} - Email: {s['email']}, Father: {s['father_phone']}, Mother: {s['mother_phone']}")

# ==== AUTH ====
def register(role):
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    if role == "student":
        append_csv(STUDENT_FILE, {"username": username, "password": password})
    else:
        append_csv(TEACHER_FILE, {"username": username, "password": password})
    print(f"{role.title()} registered.")

def login(role):
    username = input("Username: ")
    password = input("Password: ")
    records = read_csv(STUDENT_FILE if role == "student" else TEACHER_FILE)
    for r in records:
        if r["username"] == username and r["password"] == password:
            print("Login successful.")
            if role == "student":
                user = Student(username)
                if not user.get_info().get("name"):
                    user.first_time_info()
                while True:
                    print("\n1. Update Info\n2. View Notifications\n3. View Marks\n4. View Teachers\n5. Logout")
                    ch = input("Choose: ")
                    if ch == "1": user.update_info()
                    elif ch == "2": user.view_notifications()
                    elif ch == "3": user.view_marks()
                    elif ch == "4": user.view_teachers()
                    elif ch == "5": break
            else:
                user = Teacher(username)
                if not user.get_info().get("name"):
                    user.first_time_info()
                while True:
                    print("\n1. Update Info\n2. Send Notification\n3. Add Marks\n4. View Student Info\n5. Logout")
                    ch = input("Choose: ")
                    if ch == "1": user.update_info()
                    elif ch == "2": user.send_notification()
                    elif ch == "3": user.add_marks()
                    elif ch == "4": user.view_students_info()
                    elif ch == "5": break
            return
    print("Login failed.")

# ==== MAIN MENU ====
def main():
    ensure_files()
    while True:
        print("\n--- School App (CSV Based) ---")
        print("1. Student Register\n2. Student Login\n3. Teacher Register\n4. Teacher Login\n5. Exit")
        ch = input("Choose: ")
        if ch == "1": register("student")
        elif ch == "2": login("student")
        elif ch == "3": register("teacher")
        elif ch == "4": login("teacher")
        elif ch == "5": break
        else: print("Invalid option.")

if __name__ == "__main__":
    main()

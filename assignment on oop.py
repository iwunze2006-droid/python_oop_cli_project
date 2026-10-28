name = "emmanuel"
email = "emma@gmail.com"
course = "cyber security"
course_fee = 200000
is_registered = True

print (type(name))
print (type(email))
print (type(course))
print (type(course_fee))
print(type(is_registered))

name = name.upper()

print (f"congratulation {name} you are studing {course}")

# task 2
student_1 = {"name":"emmanuel", "email": "emma@gmail.com","course": "cyber security","course_fee": 200000}
student_2 = {"name":"emeka", "email": "emeka@gmail.com","course": "computer science","course_fee": 600000}
student_list = []
student_list.append(student_1)
student_list.append(student_2)
print (student_list)
# print(student_list[0]["email"])
# task 3
print(student_list[1]["email"])
def check_course_fee(course_fee):
    if course_fee > 0:
        return"Valid course fee"
    elif course_fee == 0:
        return "course is fee"
    else :
        return "ivalid course fee"
print(check_course_fee(200000)) 
print(check_course_fee(-200000))
print(check_course_fee(0))

# PART B


#task 4
class student:
    school_name = "Smart Coder Academy"
    def __init__(self, name, email, course, course_fee):
       self.name = name
       self.email = email
       self.course = course
       self.__course_fee = course_fee  # __course_fee is the number 10 encalpsulation

       # TASK 7
    def get_student_data(self):
        return{
        "name":self.name,
        "email":self.email,
        "course":self.course,
        "course_fee":self.__course_fee, # num 10
        "school":self.school_name
    } 
# task 8

    def add_student(self, student_list):
        data = self.get_student_data()
        student_list.append(data)
        print(f"{self.name} has been added successfully")

    def get_course_fee(self):                        # Task 11
        return self.__course_fee
    
    def set_course_fee(self, amount):                # Task 12
        if amount > 0:
            self.__course_fee = amount
            print(f"Course fee updated to ₦{amount}")
            return True
        else:
            print("Error: course fee must be greater than zero.")
            return False


    # task 5
student_01 = student("ezekiel","ezekiel@gmail.com","devops",30000.50)
student_02 = student("emma","emma@gmail.com","cyber security",45000.50)
student_03 = student("aisha","aisha@gmail.com","web development",65000.50)    
print(student_01.name, student_01.email,student_01.course,student_03.school_name)
print(student_01.name, student_01.email,student_01.course,student_03.school_name)
print(student_03.name, student_01.email,student_01.course,student_03.school_name)


#task 6
print(student.school_name)
print(student_01.school_name)

student_01.school_name = "another academy"
print(student_01.school_name)
print(student_02.school_name)
print(student.school_name)


#task 7
student_details_1 = student_01.get_student_data()
student_details_2 = student_02.get_student_data()
student_details_3 = student_03.get_student_data()
print(student_details_1)
print(student_details_2)
print(student_details_3)


# task 8
student_list = []
student_01.add_student(student_list)
student_02.add_student(student_list)
student_03.add_student(student_list)

# task 9



#Task 11
print(student_01.get_course_fee())
print(student_02.get_course_fee())
print(student_03.get_course_fee())

# Task 12
student_01.set_course_fee(35000)
print(student_01.get_course_fee())   # 35000
student_01.set_course_fee(-100)      # error message
student_01.set_course_fee(0)         # error message


students_list = []
student_objects = []
def find_student(student_objects, email):
    for s in student_objects:
        if s.email.lower() == email.lower():
            return s
    return None
        
def main_menu():
    print("====================================")
    print("SMARTCODER DIGITAL ACADEMY")
    print("STUDENT COURSE MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Register a student")
    print("2. View all students")
    print("3. Search for a student by email")
    print("4. Update a student's course fee")
    print("5. Exit")

    return None
while True:
    main_menu()    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        fee = float(input("Course fee: "))
        if fee < 0:
            print("Fee cannot be negative.")
        else:
            new_student = student(name, email, course, fee)
            student_objects.append(new_student)
            new_student.add_student(students_list)

    elif choice == "2":
        get_all_students(students_list)

    elif choice == "3":
        search_email = input("Enter email to search: ")
        found = None
        for s in student_objects:
            if s.email == search_email:
                found = s
        if found == None:
            print("Student not found.")
        else:
            print(found.get_student_data())

    elif choice == "4":
        search_email = input("Enter student's email: ")
        found = None
        for s in student_objects:
            if s.email == search_email:
                found = s
        if found == None:
            print("Student not found.")
        else:
            new_fee = float(input("New course fee: "))
            if found.set_course_fee(new_fee):
                for record in students_list:
                    if record["email"] == found.email:
                        record["course_fee"] = found.get_course_fee()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1 to 5.")



class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_details(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)


class BankAccount(Person):
    def __init__(self, balance, name, email, phone):
        super().__init__(name, email, phone)
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be greater than zero.")
        else:
            self.__balance = self.__balance + amount
            print(f"Deposited ₦{amount}. New balance: ₦{self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance = self.__balance - amount
            print(f"Withdrew ₦{amount}. New balance: ₦{self.__balance}")

    def get_balance(self):
        return self.__balance


# Task 14
account = BankAccount(4000, "John", "john@gmail.com", "0802233223432")
account.get_details()
print("Balance:", account.get_balance())

# Task 15 tests
account.deposit(1000)     # balance becomes 5000
account.withdraw(2000)    # balance becomes 3000
account.withdraw(5000)    # insufficient funds
account.withdraw(-500)    # invalid amount
print("Final balance:", account.get_balance())









# def show_menu():
#     print("====================================")
#     print("SMARTCODER DIGITAL ACADEMY")
#     print("STUDENT COURSE MANAGEMENT SYSTEM")
#     print("====================================")
#     print("1. Register a student")
#     print("2. View all students")
#     print("3. Search for a student by email")
#     print("4. Update a student's course fee")
#     print("5. Exit")

# def find_student(student_objects, email):
#     for s in student_objects:
#         if s.email.lower() == email.lower():
#             return s
#     return None

# def main():
#     students_list = []
#     student_objects = []

#     while True:
#         show_menu()
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Name: ")
#             email = input("Email: ")
#             course = input("Course: ")
#             try:
#                 fee = float(input("Course fee: "))
#                 if fee < 0:
#                     print("Fee cannot be negative.")
#                 else:
#                     new_student = student(name, email, course, fee)
#                     student_objects.append(new_student)
#                     new_student.add_student(students_list)
#             except ValueError:
#                 print("Invalid fee. Please enter a number.")

#         elif choice == "2":
#             get_all_students(students_list)

#         elif choice == "3":
#             found = find_student(student_objects, input("Enter email to search: "))
#             if found == None:
#                 print("Student not found.")
#             else:
#                 print(found.get_student_data())

#         elif choice == "4":
#             found = find_student(student_objects, input("Enter student's email: "))
#             if found == None:
#                 print("Student not found.")
#             else:
#                 try:
#                     new_fee = float(input("New course fee: "))
#                     if found.set_course_fee(new_fee):
#                         for record in students_list:
#                             if record["email"] == found.email:
#                                 record["course_fee"] = found.get_course_fee()
#                 except ValueError:
#                     print("Invalid fee. Please enter a number.")

#         elif choice == "5":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid option. Please choose 1 to 5.")

# main()
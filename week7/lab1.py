class Student:
    def __init__(self, student_id, last_name, programme):
        self.student_id = student_id
        self.last_name = last_name
        self.programme = programme
        self.membership_id = None
        self.withdrawn = False
 
    def register(self, membership_id):
        self.membership_id = membership_id
 
    def withdraw(self):
        self.withdrawn = True
 
class MembershipSystem:
    def __init__(self):
        self.students = {}
        self.next_membership_id = 1
        self.registered_count = 0
        self.diploma_count = 0
        self.it_count = 0
        self.withdrawn_count = 0
 
    def register_student(self, student):
        if student.student_id not in self.students:
            student.register(self.next_membership_id)
            self.students[student.student_id] = student
            self.next_membership_id += 1
            self.registered_count += 1
            if student.programme == "Bachelor of IT":
                self.diploma_count += 1
            elif student.programme == "Diploma":
                self.it_count += 1
            print(f"Student {student.last_name} registered successfully with Membership ID: {student.membership_id}")
        else:
            print(f"Student with ID {student.student_id} already exists.")
 
    def withdraw_student(self, membership_id):
        for student in self.students.values():
            if student.membership_id == membership_id and not student.withdrawn:
                student.withdrawn()
                self.registered_count -= 1
                self.withdrawn_count += 1
                if student.programme == "Bachelor of IT":
                    self.diploma_count -= 1
                elif student.programme == "Diploma":
                    self.it_count -= 1
                print(f"Student with Membership ID {membership_id} withdrawn successfully.")
                return
        print(f"Invalid Membership ID: {membership_id}")
 
    def display_registered_members(self):
        print("\nRegistered Members:")
        print(f"Total Registered Members: {self.registered_count}")
        print(f"Bachelor of IT Students: {self.it_count}")
        print(f"Diploma Students: {self.diploma_count}")
        print(f"Withdrawn Students: {self.withdrawn_count}")
 
if __name__ == "__main__":
    system = MembershipSystem()
    while True:
        print("\nMembership System Menu:")
        print("1. Register a student")
        print("2. Withdraw a student")
        print("3. Display registered members")
        print("4. Exit")
        choice = input("Enter your choice: ")
       
        if choice == '1':
            student_id = input("Enter student ID: ")
            last_name = input("Enter last name: ")
            programme = input("Enter programme (Bachelor of IT or Diploma): ")
            if programme not in ["Bachelor of IT", "Diploma"]:
                print("Invalid programme. Please enter 'Bachelor of IT' or 'Diploma'.")
                continue
            student = Student(student_id, last_name, programme)
            system.register_student(student)
       
        elif choice == '2':
            try:
                membership_id = int(input("Enter membership ID to withdraw: "))
                system.withdraw_student(membership_id)
            except ValueError:
                print("Invalid input. Please enter a numeric membership ID.")
       
        elif choice == '3':
            system.display_registered_members()
       
        elif choice == '4':
            break
       
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
 


)
 


import csv
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
class ResultSystem:
    def __init__(self):
        self.student=[]
    def add_student(self,name,roll_no,marks):
        s= Student(name, roll_no,marks)
        self.student.append(s)
    def display_all(self):
        for student in self.student:
            print('~'*50)
            print('==STUDENT REPORT==')
            print('~'*50 + '\n')
            print(f'Name = {student.name}')
            print(f"Roll No. = {student.roll_no}")
            print('Marks')
            for i,j in student.marks.items():
                print(f'{i} :{j}')
            total=0
            sub_no=0
            for i in student.marks.values():
                total +=i
                sub_no+=1
            percentage = round(total /sub_no,2)
            if percentage<=33:
                print(f'total percentage is {percentage}%, you are fail!')
            else:
                print(f'you got {percentage}%, you are pass')
            print("="*50 + "\n")
    def topper(self):
        top_student= None
        top_avg=0
        for student in self.student:
            avg= round(sum (student.marks.values())/ len(student.marks),2)
            if avg>top_avg:
                top_avg=avg
                top_student=student
        print(f"Topper : {top_student.name} with avg marks {top_avg}")
    def save_to_csv(self):
        with open ('Student.csv', "w", newline = "") as f :
            writer=csv.writer(f)
            writer.writerow(['Name', 'Roll No', 'Maths', 'Science', 'English', 'Average'])
            for student in self.student:
               avg= round(sum (student.marks.values())/ len(student.marks),2)
               writer.writerow([
                student.name,
                student.roll_no,
                student.marks['Maths'],
                student.marks['Science'],
                student.marks['English'],
                avg])
            print("CSV save ho gaya!")
    def load_from_csv(self):
        with open('students.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # header row skip karo
            for row in reader:
                print(f"Name: {row[0]}, Roll No: {row[1]}, Average: {row[5]}")

rs = ResultSystem()
name = input("Naam: ")
roll_no = int(input("Roll no: "))
marks = {}
marks['Maths'] = int(input("Maths marks: "))
marks['Science'] = int(input("Science marks: "))
marks['English'] = int(input("English marks: "))
rs.add_student(name, roll_no, marks)
rs.display_all()
rs.save_to_csv()
rs.topper()

while True:
    print("\n1. Student add karo")
    print("2. Sab display karo")
    print("3. Topper dekho")
    print("4. CSV save karo")
    print("5. CSV load karo")
    print("6. Exit")
    
    choice = input("Choice: ")
    
    if choice == '1':
        name = input("Naam: ")
        roll_no = int(input("Roll no: "))
        marks = {}
        marks['Maths'] = int(input("Maths marks: "))
        marks['Science'] = int(input("Science marks: "))
        marks['English'] = int(input("English marks: "))
        rs.add_student(name, roll_no, marks)
        print("Student add ho gaya!")
    elif choice == '2':
        rs.display_all()
    elif choice == '3':
        rs.topper()
    elif choice == '4':
        rs.save_to_csv()
    elif choice == '5':
        rs.load_from_csv()
    elif choice == '6':
        break

# class Animal():
#     def __init__(self,laqabi,yoshi):
#         self.laqabi=laqabi
#         self.yoshi=yoshi
#     def getinfo(self):
#         return f"yoshi={self.yoshi},laqabi={self.laqabi}"
# class Mushuk(Animal):
#     def __init__(self,yoshi,laqabi,zoti,wherefrom):
#       super().__init__(laqabi,yoshi)
#       self.zoti=zoti
#       self.wherefrom=wherefrom
#     def getinf0(self):
#         return super().getinfo()+f" zoti={self.zoti},qayerdanligi={self.wherefrom}"
    
# mushukcha=Mushuk(13,"koshkamrus","rus brilyandi","rossiya")
# print(mushukcha.getinf0())

# class Restaurant():
#     def __init(self,menu_items:list,book_table,customer_order):
#         self.menu=menu_items
#         self.book_table=[]
#         self.customer_order={}
#     def add_item_to_menu(self,item):
#         self.add_item_to_menu.append(item)
#     def book_tables(self,number):
#         if number  not in self.book_table:
#             self.book_table.append(number)
#             return f"suhbu {number}chi stol  muvaffaqiyatli  band qilindi"
#         return "ushbu stol boshqa tomonidan band qilingan"
#     def book_tables(self):
#         ...

class Student():
    def __init__(self,phone_number,name,age):
        self.phone_number=phone_number
        self.name=name
        self.age=age
class Course():
    def __init__(self,price,title,duration,student_limit):
        self.students=[]
        self.price=price
        self.title=title
        self.duration=duration
        self.student_limit=student_limit
    def add_student(self,studentinfo):
        print(studentinfo not in self.students)
        print(len(self.students)<self.student_limit, self.students, self.student_limit)
        if (studentinfo not in self.students) and len(self.students)<self.student_limit:
            self.students.append(studentinfo)
            return "siz kursga muvaffaqiyatli qo`shildingiz"
        return "bu kurs to`lgan"
student1=Student("+998900914478","Asror",21)
student2=Student("+998900904478","Ahror",22)
student3=Student("+998900924478","Abror",23)
studen4=Student("+998900924477","kamol",24)

python=Course(1200000,"python backend","8oy",3)
print(python.add_student(student1))
print(python.add_student(student2))
print(python.add_student(student3))
print(python.add_student(studen4))
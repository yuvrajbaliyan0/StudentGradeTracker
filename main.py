#The APP
class StudentGradeTracker:
    def __init__(self):
        self.studentData = []
    

#Student Data 
class Student:
    def __init__(self,Name,Subject,Mark):
        self.name = Name
        self.subject = Subject
        self.mark = Mark
    

tracker = StudentGradeTracker()

#Student1 
baldeep = Student("Baldeep","English",90)
baldeep2 = Student("Baldeep","Maths",80)


#Student2
tanya = Student("Tanya","English",50)
tanya2 = Student("Tanya","Maths",70)

#Student3
gaytri = Student("Gaytri","English",95)
gaytri2 = Student("Gaytri","Maths",80)

#Student4
hitesh = Student("Hitesh","English",40)
hitesh2 = Student("Hitesh","Maths",35)


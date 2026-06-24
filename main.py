#The APP
class StudentGradeTracker:
    def __init__(self):
        self.studentData = []
    
    #ADD FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def add_function(self,Student):
        self.studentData.append(Student)

    #DELETE FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def delete_function(self,Student):
        self.studentData.remove(Student)
    
    #AVG OF GRADE FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def avg_function(self):
        return sum(student.mark for mark in self.studentData)/ len(self.studentData)
    
    #FILTER BY SUBJECT FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def filter_function(self,Subject):
        filterlist =[]
        for student in self.studentData:
            if student.subject == Subject:
                filterlist.append(student)
        return filterlist
    
    

#Student Data 
class Student:
    def __init__(self,Name,Subject,Mark):
        self.name = Name
        self.subject = Subject
        self.mark = Mark
    
    def __str__(self):
        return f"NAME :{self.name},   SUBJECT :{self.subject},   MARKS :{self.mark}"
    

tracker = StudentGradeTracker()

#ADD STUDENT MARKS IN LIST.....................................................................................
#Student1 
baldeep = Student("Baldeep","English",90)
baldeep2 = Student("Baldeep","Maths",80)
tracker.add_function(baldeep)
tracker.add_function(baldeep2)


#Student2
tanya = Student("Tanya","English",50)
tanya2 = Student("Tanya","Maths",70)
tracker.add_function(tanya)
tracker.add_function(tanya2)

#Student3
gaytri = Student("Gaytri","English",95)
gaytri2 = Student("Gaytri","Maths",80)
tracker.add_function(gaytri)
tracker.add_function(gaytri2)

#Student4
hitesh = Student("Hitesh","English",40)
hitesh2 = Student("Hitesh","Maths",35)
tracker.add_function(hitesh)
tracker.add_function(hitesh2)

#DELETE STUDENT MARKS FROM LIST..................................................................................
tracker.delete_function(hitesh)
tracker.delete_function(hitesh2)


#GET STUDENTS DATA FROM LIST......................................................................................
for student in tracker.studentData:
    print(student)

#GET AVERAGE OF ALL STUDENT MARKS.................................................................................
avg = tracker.avg_function()
print(f"Average Of Students Marks is {avg}\n")



for filteredlist in tracker.filter_function("English"):    
    print(f"Students With English Marks are: \n{filteredlist}\n")

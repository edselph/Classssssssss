class Person():
    def __init__(self,name,address,numbercourse,course):
        self.name = name
        self.address = address
        self.numbercourse = numbercourse
        self.course = course
    
class student(Person):
    def __init__(self,CourseGrade):
        self.CourseGrade = CourseGrade

    def Average():
       return (self.CourseGrade/self.numbercourse)

    super().__init__()
    
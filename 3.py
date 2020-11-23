class Person():
    def __init__(self,name,address):
        self.__name = name
        self.__address = address
    
    def GetName(self):
        return self.__name

    def GetAddress(self):
        return self.__address

    def SetAddress(self,address):
        self.__address = address

    def __str__(self):
        return self.GetName() + "(" + self.GetAddress() + ")"        
    
class student(Person):

    def __init__(self,name,address,numcourse = 0,course =[],grade = []):
        super().__init__(name, address)
        self.__numcourse = numcourse
        self.__course = course
        self.__grade = grade


    def addcoursegrade(self,course,grade):
        self.__course.append(course)
        self.__grade.append(grade)

    def printgrade(self):
        print(self.__grade)

    def Average():
       return (sum(self.__grade)/len(self.grade))

class teacher(Person):
    course = []
    def addcoursegrade(self,course):
        if self.course() not in course:
            course.append(self.__course())
        else:
            print("There's already courses")
    
    def removecourse(self,course):
        if self.__course() in course:
            course.remove(self.course())
            return   

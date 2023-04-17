class Student():
    name = ''
    age = 0
    __weight = 100

    def sleep(self):
        print('{}的体重是{}'.format(self.name,self.__weight))
    def get_weight(self):
        return self.__weight
    def ser_weight(self,w):
        self.__weight = w
        
student = Student()
student.name = 's'
student.age = 21
print(student)
student1 = Student('蔡萌',20)
print(student1)
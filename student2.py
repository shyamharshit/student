class student: 
    grade = 10
    name = "pengiuin"

    def introduction(self) :
        print("hi i am a student")


    def detail(self) :
        print("my name is",self.name)
        print("i study in grade",self.grade)

ob = student()
ob.introduction()
ob.detail()        
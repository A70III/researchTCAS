class InputUniversity():
    def __init__(self):
        self.major1 = 0
        self.major2 = 0
        self.major3 = 0
        self.major4 = 0
        self.major5 = 0
        self.major6 = 0
        self.univerName = ""

    def MajorInit(self, major1, major2, major3, major4, major5, major6):
        self.major1 = major1
        self.major2 = major2
        self.major3 = major3
        self.major4 = major4
        self.major5 = major5
        self.major6 = major6
        print( major1, major2, major3, major4, major5, major6)
        

    def UniversityName(self, univerName):
        self.univerName = univerName
        print(univerName)



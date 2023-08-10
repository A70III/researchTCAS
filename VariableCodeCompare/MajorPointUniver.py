

class InputUniversity():
    
    def __init__(self):
        self.major1 = 0
        self.major2 = 0
        self.major3 = 0
        self.major4 = 0
        self.major5 = 0
        self.major6 = 0
        self.univerName = ""
        self.groupPointMajor = []
        self.countUni = 0
    
    def groupMajorPoint(self,university_name):
        
        self.university_name = university_name
        import numpy as np
        pointMajor = np.zeros(6, dtype=float)

        for _ in range(6):
            setPoint = float(input("Input Score: "))
            pointMajor[_] = setPoint

        self.groupPointMajor.insert(self.countUni,pointMajor)
        
        pointMajor = np.zeros(6, dtype=float)
        self.countUni  += 1
    



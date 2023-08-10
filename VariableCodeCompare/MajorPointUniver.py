class InputUniversity():
    
    def __init__(self):
        self.university_name = ""
        self.groupPointMajor = []
        self.countUni = 0
    
    def groupMajorPoint(self,university_name):
        
        import numpy as np
        pointMajor = []

        for _ in range(6):
            setPoint = float(input("Input Score: "))
            pointMajor.insert(_,setPoint)

        self.groupPointMajor.insert(self.countUni,pointMajor)
        
        pointMajor = []
        self.countUni  += 1
    



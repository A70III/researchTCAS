class InputMajorCriteria():
    
    def __init__(self):
        self.university_name = ""
        self.groupPoint = []
        self.countUni = 0
    
    def groupMajorPoint(self,university_name):
        
        import numpy as np
        pointMajor = []

        for _ in range(6):
            setPoint = float(input("Input Major Criteria Score : "))
            pointMajor.insert(_,setPoint)

        self.groupPoint.insert(self.countUni,pointMajor)
        
        pointMajor = []
        self.countUni  += 1
    



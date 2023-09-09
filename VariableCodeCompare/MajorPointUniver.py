class InputMajorCriteria:
    def __init__(self):
        self.university_name = ""
        self.groupPoint = []
        self.countUni = 0
    
    def groupMajorPoint(self, university_name):
        pointMajor = []

        PointLang = float(input("Input Language Score: "))
        pointMajor.append(PointLang)
        PointThink = float(input("Input Thinking Score: "))
        pointMajor.append(PointThink)
        PointArt = float(input("Input Arts and Society Score: "))
        pointMajor.append(PointArt)
        PointSci = float(input("Input Science Score: "))
        pointMajor.append(PointSci)
        PointMath = float(input("Input Mathematics Score: "))
        pointMajor.append(PointMath)
        PointGen = float(input("Input General Score: "))
        pointMajor.append(PointGen)

        self.groupPoint.append(pointMajor)
        self.countUni += 1
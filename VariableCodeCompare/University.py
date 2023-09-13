class University:
    def __init__(self) -> None:
        self.NameUni = input("ชื่อสถาบัน : ")  # ชื่อสถาบัน
        #self.CampusName = input("ชื่อวิทยาเขต : ") #ชื่อวิทยาเขต
        #self.FacultyName = input("ชื่อคณะ : ") #ชื่อคณะ
        #self.CourseName = input("ชื่อหลักสูตร : ") #ชื่อหลักสูตร
        #self.About = input("รายละเอียด : ") #รายละเอียด
        
        self.MajorScore = [
            float(input("Input Language Score: ")),
            float(input("Input Thinking Score: ")),
            float(input("Input Arts and Society Score: ")),
            float(input("Input Science Score: ")),
            float(input("Input Mathematics Score: ")),
            float(input("Input General Score: ")),
        ]
        

        #self.LangScr = float(input("Input Language Score: "))
        #self.ThinkScr = float(input("Input Thinking Score: "))
        #self.ArtScr = float(input("Input Arts and Society Score: "))
        #self.SciScr = float(input("Input Science Score: "))
        #self.MathScr = float(input("Input Mathematics Score: "))
        #self.GenScr = float(input("Input General Score: "))
    
        
        
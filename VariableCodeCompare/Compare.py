from UniversityName import UniverName
from MajorPointUniver import InputMajorCriteria
from Radar import RadarCompare

univer_name_obj = UniverName()
major_obj = InputMajorCriteria()
radar_obj = RadarCompare()
countUni=0

print("Welcome to University Compare Major Criteria Score System! (Max 10 University)")
starts = input("Start to Input Major Criteria Score? (Y/N): ")
if starts.upper() == "N":
    print("End of Program.")
else:
    while True:
    
        univer_name_obj.InputUniName(starts)#เริ่มรับชื่อมหาลัย เก็บในlist
        print(univer_name_obj.groupUniName[countUni])
        
        major_obj.groupMajorPoint(univer_name_obj.groupUniName[countUni])#รับแต้มพร้อมเลือกมหาลัย(ตามตำแหน่งลำดับในlist)
    
        print(major_obj.groupPoint)
        countUni +=1
        
        if countUni==10:
            break

        continueInput = input("Input Another University Criteria? (Y/N): ")
        if continueInput.upper() == "N":
            break
        
        
        
radar_obj.PlotRadar(univer_name_obj.groupUniName,major_obj.groupPoint)


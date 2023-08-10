from UniversityName import UniverName
from MajorPointUniver import InputUniversity
from Radar import RadarCompare
import numpy as np
import matplotlib.pyplot as plt

univer_name_obj = UniverName()
major_obj = InputUniversity()
radar_obj = RadarCompare()
countUni=0

starts = input("Start to Input Score? (Y/N): ")
if starts.upper() == "N":
    print("END of Program")
else:
    while True:
    
        univer_name_obj.InputUniName(starts)
        print(univer_name_obj.groupUniName[countUni])
        
        major_obj.groupMajorPoint(univer_name_obj.groupUniName[countUni])
    
        print(major_obj.groupPointMajor)

        continueInput = input("Input Another University Criteria (Y/N): ")
        if continueInput.upper() == "N":
            break
        countUni +=1
        
radar_obj.PlotRadar(univer_name_obj.groupUniName,major_obj.groupPointMajor)


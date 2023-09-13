from University import University
from RadarGraph import RadarGraph

UniversityList =[]
radar_obj = RadarGraph()

for i in range(10):
    inputUniversity = University()
    UniversityList.append(inputUniversity)
    
    continueInput = input("Input Another University Criteria? (Y/N): ")
    if continueInput.upper() == "N":
        break
    
radar_obj.PlotRadar(UniversityList)
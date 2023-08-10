from UniversityName import UniverName
from MajorPointUniver import InputUniversity

univer_name_obj = UniverName()
input_university_obj = InputUniversity()
countUni=0

starts = input("Start to Input Score? (Y/N): ")
if starts.upper() == "N":
    print("END of Program")
else:
    while True:
    
        univer_name_obj.InputUniName(starts)
        print(univer_name_obj.groupUniName[countUni])
        
        input_university_obj.groupMajorPoint(univer_name_obj.groupUniName[countUni])
    
        print(input_university_obj.groupPointMajor)

        continueInput = input("Input Another University Criteria (Y/N): ")
        if continueInput.upper() == "N":
            break
        countUni +=1
print(univer_name_obj.groupUniName)

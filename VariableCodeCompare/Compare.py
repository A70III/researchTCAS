from InputUniversity import InputUniversity
import numpy as np

groupMajorUni = np.array('i',[])
countUniver=0
while(True):
    groupMajorPoint = np.array('i',[])
    for _ in range(6):
        setPoint = int(input("Input Score: "))
        groupMajorPoint.append(setPoint)  # Append scores to the 1D array

    groupMajorUni.append(groupMajorPoint)  # Append the 1D array to the 2D array

    ConInput = input("Input Another University Criteria (Y/N): ")
    if ConInput.upper() == "N":
        break

print(groupMajorUni)
#def InputMajorPoint():
    #major1 = int(input("Input Language Score: "))
   # major2 = int(input("Input Thinking Score: "))
   # major3 = int(input("Input Arts and Society Score: "))
    ##major4 = int(input("Input Science Score: "))
  #  major5 = int(input("Input Mathematics Score: "))
   # major6 = int(input("Input General Score: "))
   # return major1, major2, major3, major4, major5, major6

test = InputUniversity()
#major1, major2, major3, major4, major5, major6 = InputMajorPoint()
test.MajorInit(groupMajorPoint[0],groupMajorPoint[1],groupMajorPoint[2],groupMajorPoint[3],groupMajorPoint[4],groupMajorPoint[5])
print(test.MajorInit)
print()

from InputUniversity import InputUniversity

def InputMajorPoint():
    major1 = int(input("Input Language Score: "))
    major2 = int(input("Input Thinking Score: "))
    major3 = int(input("Input Arts and Society Score: "))
    major4 = int(input("Input Science Score: "))
    major5 = int(input("Input Mathematics Score: "))
    major6 = int(input("Input General Score: "))
    return major1, major2, major3, major4, major5, major6

test = InputUniversity()
major1, major2, major3, major4, major5, major6 = InputMajorPoint()
test.MajorInit(major1, major2, major3, major4, major5, major6)
print(test.MajorInit)

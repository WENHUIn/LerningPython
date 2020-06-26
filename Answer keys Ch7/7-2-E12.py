def main():
    ## Calculate semester grades.
    listOfStudents = obtainListOfStudents()  # students and grades
    displayResults(listOfStudents)

def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter student's name: ")
        midterm = float(input("Enter student's grade on midterm exam: "))
        final = float(input("Enter student's grade on final exam: "))
        category = input("Enter category (LG or PF): ")
        if category.upper() == "LG":
            st = LGstudent(name, midterm, final)
        else:
            status = input("Are you a full-time student (Y/N)? ")
            if status.upper() == 'Y':
                fullTime = True
            else:
                fullTime = False
            st = PFstudent(name, midterm, final, fullTime)
        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfStudents

def displayResults(listOfStudents):
    print("\nNAME\tGRADE\tSTATUS")
    listOfStudents.sort(key = lambda x: x.getName())
    for pupil in listOfStudents:
        print(pupil)

class Student:
    def __init__(self, name="", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final = final
        self._semesterGrade = ""
      
    def setName(self, name):
        self._name = name

    def setMidterm(self, midterm):
        self._midterm = midterm

    def setFinal(self, final):
        self._final = final

    def getName(self):
        return self._name

    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()
       
class LGstudent(Student):
    
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (self._name + "\t" + self.calcSemGrade() +
               "\tFull-time student")

class PFstudent(Student):
    def __init__(self, name="", midterm=0, final=0, fullTime=True):
        super().__init__(name, midterm, final)
        self._fullTime = fullTime

    def setFullTime(self, fullTime):
        self._fullTime = fullTime

    def getFullTime(self):
        return self._fullTime
        
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 60:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        if self._fullTime:
            status = "Full-time student"
        else:
            status = "Part-time student"                
        return (self._name + "\t" + self.calcSemGrade()
                 + "\t" + status)

main()



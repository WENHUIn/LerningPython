def main():
    ## Calculate an average.
    listOfGrades = []
    for i in range(6):
        quizGrade = float(input("Enter grade on quiz " + \
                                str(i + 1) + ": "))
        listOfGrades.append(quizGrade)
    q = Quizzes(listOfGrades)    
    print(q)
    
class Quizzes:
    def __init__(self, listOfGrades):
        self._quizGrades = listOfGrades
        
    def average(self):
        self._quizGrades.sort()
        self._quizGrades = self._quizGrades[1:]    # Drop lowest quiz grade.
        return sum(self._quizGrades) / 5

    def __str__(self):
        return "Quiz average: " + str(self.average())
                                    
main()    

def gradingStudents(grades):
    
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        elif (grade+2)%5==0:
            new_grades.append(grade+2)
        elif (grade+1)%5==0:
            new_grades.append(grade+1)
        else:
            new_grades.append(grade)
            
    return new_grades
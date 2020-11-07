FILENAME1 = 'scores.txt'
READ_MODE = 'r'
FILENAME2 = 'grade.txt'
WRITE_MODE = 'w'
try:
    with open(FILENAME1) as names_file1:
        pass
except IOError as error:
    print(f'Unable to open file {FILENAME1}. Error message: {error}')
print('After the handling code, program keeps running')
grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0
grade_F = 0
grade_count = 0
total_student = 0
total_score = 0
names_file1 = open(FILENAME1,READ_MODE)
names_file2 = open(FILENAME2,WRITE_MODE)
with names_file1, names_file2:
    for line in names_file1:
        info= line.split()
        try:
            if int(info[2])>=90:
                print(f'{info[0]} {info[1]} has a grade A')
                names_file2.write(f'{info[0]} {info[1]} A.\n')
                grade_A +=4.0
                grade_count +=1
            elif int(info[2])>=80:
                print(f'{info[0]} {info[1]} has a grade B')
                names_file2.write(f'{info[0]} {info[1]}  B.\n')
                grade_B += 3
                grade_count +=1
            elif  int(info[2])>=70:
                print(f'{info[0]} {info[1]} has a grade C')
                names_file2.write(f'{info[0]} {info[1]} C.\n')
                grade_C +=2
                grade_count +=1
            elif int(info[2])>=60:
                print(f'{info[0]} {info[1]} has a grade D')
                names_file2.write(f'{info[0]} {info[1]} D.\n')
                grade_D += 1
                grade_count +=1
            else:
                print(f'{info[0]} {info[1]} has a grade F')
                names_file2.write(f'{info[0]} {info[1]} F.\n')
                grade_F += 0
                grade_count +=1
        except ValueError as error:
            names_file2.write(f'Bad score value for {info[0]}, ignored.\n')
    GPA = (grade_A +grade_B +grade_C+grade_D+grade_F)/grade_count

    if grade_count != 0:
        names_file2.write(f'The class GPA is {GPA:.2f}')
        print(f'The class GPA is {GPA:.2f}')
    else:
        names_file2.write(f'ZeroDivisionError: divide by zero exception')
        print(f'ZeroDivisionError: divide by zero exception')
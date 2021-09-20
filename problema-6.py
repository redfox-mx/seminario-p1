from util.question import OK_QUESTION
from util.log import clear, message, question, section, divider, trim

def new_student():
    clear()
    section('NUEVO ALUMNO')
    name = question('Nombre del Alumno: ')
    final = 0
    for i in range(1, 4):
        grade = question(f'Calificacion parcial {i}: ', to=float)
        if grade >= 7:
            final += grade
        else:
            message('El alumno no aprobo, para que preocuparse')
            return (name, 'NA')
    
    return (name, final / 3)

students = [new_student()]
while question('REGISTRAR NUEVO ALIMNO?', qtype=OK_QUESTION):
    students.append(new_student())

clear()
divider(32)
message(f'{"ALUMNO":^20}{"CALIFICACION":^12}')
divider(32)
for student, grade in students:
    student = trim(student, 20)
    message(f'{student:20}', end='')
    message(f'{grade:^12.2f}' if isinstance(grade, float) else f'{grade:^12}')
divider(32)
message(f'Total {len(students)} alumnos')
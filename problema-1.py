from util.log import question, message

message('Programa para aprender las tablas de multiplicar')
n = question('Con que numero queres empezar? ', to=int)

correctness = 0
for i in range(1, 11):
    ans = question(f'{n} * {i} = ', to=int)
    if ans == n * i:
        correctness += 1
        message('Valor Correcto')
    else:
        message(f'El valor correcto es {i * n}')

message(f'Has acertado {correctness} de 10')

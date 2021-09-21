from core.table import Table
from core.report import Report
from util.log import message, question, clear, section, OK_QUESTION

data = Table('PERSONAS', 'PESO')

def add(table: Table):
    clear()
    section('AÑADIR VIAJE')
    c = question('Cantidad de personas: ', to=int)
    p = question('Peso total: ', to=float)
    table.append(c, p)

add(data)
while question('Nuevo viaje?', qtype=OK_QUESTION):
    add(data)

report = Report(data)
report.show()
ppv, wpv = data.as_ndarray().mean(axis=0)
n = len(data.get_table())
p, w = data.as_ndarray().sum(axis=0)
report.footer(f'Numero de viajes {n}')
report.footer(f'Perosnas transportadas {p}')
report.footer(f'Peso transpportado {w}')
report.footer(f'Personas promedio por viaje {ppv}')
report.footer(f'Peso promedio por viaje {wpv}')
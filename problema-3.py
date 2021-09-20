from core.table import Table
from core.report import Report
from util.log import message, question, clear, section, OK_QUESTION

data = Table('ARTICULOS', 'CCOSTO DE PRODUCCION', 'UTILIDAD', 'IMPUESTO', 'PRESION DE VENTA')

def add(table: Table):
    clear()
    section('AÑADIR PRODUCTO')
    des = question('Descripcio: ')
    cp = question('Costo de produccion: ', to=float)
    u = cp * 1.2
    i = u * (cp + u)
    pv = cp + u + i
    table.append(des, cp, u, i, pv)

add(data)
while question('Añadir producto?', qtype=OK_QUESTION):
    add(data)

report = Report(data)
clear()
report.show(full=True)

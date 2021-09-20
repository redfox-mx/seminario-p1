from core.table import Table
from core.report import Report
from util.log import message, question, clear, section, OK_QUESTION

data = Table('ARTICULOS', 'CANTIDAD', 'PRECIO UNITARIO', 'TOTAL')

def add(table: Table):
    clear()
    section('AÑADIR PRODUCTO')
    des = question('Descripcio: ')
    c = question('Cantidad: ', to=int)
    pu = question('Precio unitario: ', to=float)
    t = c * pu
    table.append(des, c, pu, t)

name = question('Nombre: ')
add(data)
while question('Añadir producto?', qtype=OK_QUESTION):
    add(data)

report = Report(data)
clear()
message(f'cliente {name.upper()}')

report.show()
subtotal = data.as_ndarray()[:,-1].astype(float).sum(axis=0)
report.footer(f'subtotal {float(subtotal):.2f}', align='right')
impuesto = subtotal * .15
report.footer(f'impuesto {float(impuesto):.2f}', align='right')
total = impuesto + subtotal
report.footer(f'total {float(total):.2f}', align='right')
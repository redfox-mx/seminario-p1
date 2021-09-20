from core.table import Table
from core.report import Report
from util.log import message, question, clear, section, OK_QUESTION

def add(table: Table):
    clear()
    section('AÑADIR PRODUCTO')
    des = question('Descripcio: ')
    c = question('Cantidad: ', to=int)
    pu = question('Precio unitario: ', to=float)
    t = c * pu
    table.append(des, c, pu, t)

def new_client():
    data = Table('ARTICULOS', 'CANTIDAD', 'PRECIO UNITARIO', 'TOTAL')
    name = question('Nombre: ')
    add(data)
    while question('Añadir producto?', qtype=OK_QUESTION):
        add(data)
    
    return (name, data)

def show_report(name, data):
    report = Report(data)
    message(f'cliente {name.upper()}')

    report.show()
    subtotal = data.as_ndarray()[:,-1].astype(float).sum(axis=0)
    report.footer(f'subtotal {float(subtotal):.2f}', align='right')
    impuesto = subtotal * .15
    report.footer(f'impuesto {float(impuesto):.2f}', align='right')
    total = impuesto + subtotal
    report.footer(f'total {float(total):.2f}', align='right')

people = [new_client()]

while question('Agrgar otro cliente?', qtype=OK_QUESTION):
    people.append(new_client())

for name, data in people:
    message('')
    show_report(name, data)
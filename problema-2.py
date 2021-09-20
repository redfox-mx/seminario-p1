from core.table import Table
from core.report import Report
from util.log import message, question, clear, section, OK_QUESTION

data = Table('ARTICULOS', 'UNIDADES PRODUCIDAS', 'FACTOR COSTO', 'COSTO FIJO', 'COSTO DE PRODUCCION')

def add(table: Table):
    clear()
    section('AÑADIR PRODUCTO')
    des = question('Descripcio: ')
    up = question('Unidades producidas: ', to=int)
    fc = question('Factor costo: ', to=float)
    cf = question('Costo fijo: ', to=float)
    cp = up * fc + cf
    table.append(des, up, fc, cf, cp)

while question('Añadir producto?', qtype=OK_QUESTION):
    add(data)

report = Report(data)
report.show()







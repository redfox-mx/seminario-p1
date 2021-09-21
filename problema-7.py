from core.report import Report
from core.table import Table
from util.log import question, message, OK_QUESTION

def new_movement():
    m = question('Movimiento [+ deposito, - retiro]: ', to=float)
    if m >= 0:
        return (m, 0)
    
    return (0, m)

def register_movement(table: Table, saldo):
    deposito, retiro = new_movement()
    saldo = saldo + retiro + deposito
    n = len(table.get_table())
    table.append( 1 if n == 0 else int(table.as_ndarray()[-1,0] + 1), deposito, retiro, saldo)
    return saldo

history = Table('MOVIMINETOS', 'DEPOSITOS', 'RETIROS', 'TOTAL')
name = question('NOMBRE: ')

saldo = question('SALDO INICIAL: ', to=float)
saldo = register_movement(history, saldo)

while question('DESEA REALIZAR OTRO MOVIMIENTO?', qtype=OK_QUESTION):
    saldo = register_movement(history, saldo)

rep = Report(history)
rep.show()
message(f'{"Totales":^20}', end='')
depositos = history.get_col("DEPOSITOS").sum()
message(f'{depositos:^20}', end='')
retiros = -1 * history.get_col('RETIROS').sum()
message(f'{retiros:^20}', end='')
total = history.get_col('TOTAL')[-1]
message(f'{total:^20}')

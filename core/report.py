from core.table import Table
from util.log import message

class Report():
    def __init__(self, table: Table, size=20):
        self.table = table
        self.WIDTH = len(table.headings()) * size
        self.FIEL_WIDTH = size

    def show(self):
        message(self.WIDTH * '-')
        for key in self.table.headings():
            message(f'{key:^20}', trimed=True, end='', size=self.FIEL_WIDTH)
        message('')
        
        message(self.WIDTH * '-')
        for row in self.table.get_table():
            for element in row:
                if isinstance(element, int):
                    message(f'{element:^{self.FIEL_WIDTH}}', end='')
                elif isinstance(element, float):
                    message(f'{element:^{self.FIEL_WIDTH}.2f}', end='')
                else:
                    message(f'{element:{self.FIEL_WIDTH}}', trimed=self.FIEL_WIDTH, end='')
            message('')

        message(self.WIDTH * '-')



from core.table import Table
from util.log import message, trim, divider

class Report():
    def __init__(self, table: Table, size=20):
        self.table = table
        self.WIDTH = len(table.headings()) * size
        self.FIEL_WIDTH = size

    def show(self, full=False):
        divider(self.WIDTH)
        for key in self.table.headings():
            message(f'{key:^20}', trimed=True, end='', size=self.FIEL_WIDTH)
        message('')

        divider(self.WIDTH)
        for row in self.table.get_table():
            for element in row:
                if isinstance(element, int):
                    message(f'{element:^{self.FIEL_WIDTH}}', end='')
                elif isinstance(element, float):
                    message(f'{element:^{self.FIEL_WIDTH}.2f}', end='')
                else:
                    message(f'{element:{self.FIEL_WIDTH}}', trimed=self.FIEL_WIDTH, end='')
            message('')

        divider(self.WIDTH)
        if full:
            self._show_full_()
            message('')
            divider(self.WIDTH)
    
    def _show_full_(self):
        total = 'Total ' + str(len( self.table.get_table() ))
        message(f'{total:{self.FIEL_WIDTH}}', end='')
        arr = self.table.as_ndarray()[:,1:].astype(float)
        for element in arr.sum(axis=0):
            element = float(element)
            message(f'{element:^{self.FIEL_WIDTH}.2f}', end='')

    def footer(self, slice: str, align='left'):
        slice = trim(slice, size=self.WIDTH)
        if align == 'center':
            message(f'{slice:^{self.WIDTH}}')
        elif align == 'right':
            message(f'{slice:>{self.WIDTH}}')
        else:
            message(f'{slice:{self.WIDTH}}')




from numpy import array

class Table():

    def __init__(self, *headings):
        pos = 0
        self.arr = []
        self.titles = {}
        for i, title in enumerate(headings):
            self.titles[title] = i
    
    def as_ndarray(self):
        return array(self.arr)

    def get_table(self):
        return self.arr

    def append(self, *args):
        self.arr.append(args)
    
    def headings(self):
        return self.titles.keys()
    
    def get_col(self, colname):
        return self.as_ndarray()[:,self.titles[colname]]
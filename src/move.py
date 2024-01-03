
class Move:

    def __init__(self, initial, final):
        # inital and final are squares
        self.inital = initial
        self.final = final

    def __str__(self):
        s = ''
        s += f'({self.inital.col},{self.inital.row})'
        s += f' -> ({self.final.col},{self.final.row})'
        return s
    
    def __eq__(self, other):
        return self.inital == other.inital and self.final == other.final
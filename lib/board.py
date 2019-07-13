class Board(object):
    """
    盤。セルは持たない。
    """

    def __init__(self):
        self.width = 19
        return

    def brute_force(self, callback):
        """
        四角形 総当たり
        """
        for y in reversed(range(0, self.width-1)):
            for x in range(0, self.width-1):
                for y2 in range(y+1, self.width):
                    for x2 in range(x+1, self.width):
                        callback(x, y, x2, y2)

    def iter(self, cell_callback, line_callback):
        for y in reversed(range(0, self.width)):
            for x in range(0, self.width):
                cell_callback(x, y)
            line_callback(x, y)

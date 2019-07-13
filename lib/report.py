from lib.board import Board


def new_key(x, y, x2, y2):
    return ((x*1000 + y) * 1000 + x2)*1000 + y2


class Report(object):
    """
    計算結果。
    """

    def __init__(self):
        self.dict = {}
        self.sum_succeed = 0
        self.sum_failed = 0

    def new_item(self, key):
        self.dict[key] = {"succeed": 0, "failed": 0}

    def increase_cell(self, key, prop_name, offset):
        if key not in self.dict:
            self.new_item(key)

        self.dict[key][prop_name] += offset

    def init_cell(self, x, y, x2, y2):
        key = new_key(x, y, x2, y2)
        self.new_item(key)

    def sum_cell(self, x, y, x2, y2):
        key = new_key(x, y, x2, y2)
        self.sum_succeed += self.dict[key]["succeed"]
        self.sum_failed += self.dict[key]["failed"]
        return

    def show(self, board):
        self.sum_succeed = 0
        self.sum_failed = 0
        board.brute_force(self.sum_cell)
        print("Succeed : {}".format(self.sum_succeed))
        print("Failed  : {}".format(self.sum_failed))

        total = self.sum_succeed + self.sum_failed
        print("total   : {}".format(total))

        if 0 < total:
            rate = (self.sum_succeed)/total
            print("Rate    : {:>.4f}".format(rate))

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

    def sum(self, board):
        self.sum_succeed = 0
        self.sum_failed = 0

        def sum_cell(x, y, x2, y2):
            key = new_key(x, y, x2, y2)
            self.sum_succeed += self.dict[key]["succeed"]
            self.sum_failed += self.dict[key]["failed"]
            return

        board.brute_force(sum_cell)

        total = self.sum_succeed + self.sum_failed

        rate = None
        if 0 < total:
            rate = (self.sum_succeed)/total

        return {
            "succeed": self.sum_succeed,
            "failed": self.sum_failed,
            "total": total,
            "rate": rate,
        }

    def show(self, board):
        sum_dict = self.sum(board)

        print("Succeed : {}".format(sum_dict["succeed"]))
        print("Failed  : {}".format(sum_dict["failed"]))
        print("total   : {}".format(sum_dict["total"]))
        print("Rate    : {:>.4f}".format(sum_dict["rate"]))

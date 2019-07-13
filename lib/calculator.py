from lib.board import Board
from lib.report import new_key
from lib.report import Report


class Calculator(object):
    def __init__(self, is_red_zone):
        self.is_red_zone = is_red_zone
        self.report = Report()
        return

    def calculate(self):
        board = Board()
        board.brute_force(self.report.init_cell)
        board.brute_force(self.try_match_rectangle)
        self.report.show()
        return

    def show_table(self):
        for y in reversed(range(0, 19)):
            for x in range(0, 19):
                if self.is_red_zone(x, y):
                    print("[.] ", end="")
                else:
                    print(" .  ", end="")
            print("")

    def try_match_rectangle(self, x, y, x2, y2):
        """
        四角形を置いてみるぜ☆（＾～＾）
        """
        key = new_key(x, y, x2, y2)

        # 左上角、右下角、左下角　はレッドゾーンの外にあること。
        # 右上角はレッドゾーンの中にあること。
        if not self.is_red_zone(x, y2) and not self.is_red_zone(x2, y) and not self.is_red_zone(x, y) and self.is_red_zone(x2, y2):
            self.report.increase_cell(key, "succeed", 1)
        else:
            self.report.increase_cell(key, "failed", 1)

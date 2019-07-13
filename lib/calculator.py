from lib.board import Board
from lib.report import new_key
from lib.report import Report


class Calculator(object):
    def __init__(self, width=19, height=19):
        def is_red_zone(x, y):
            """
            右上の足だけが踏めるマス。
            """

            return x == y

        self.is_red_zone = is_red_zone
        self.report = Report()
        self.board = Board(width, height)
        return

    def set_red_zone(self, is_red_zone):
        self.is_red_zone = is_red_zone

    def calculate(self):
        self.board.brute_force(self.report.init_cell)
        self.board.brute_force(self.try_match_rectangle)

    @property
    def board_width(self):
        return self.board.width

    @property
    def board_height(self):
        return self.board.height

    def get_report_sum(self):
        return self.report.sum(self.board)

    def show_report(self):
        self.report.show(self.board)

    def show_table(self):
        def cell_callback(x, y):
            if self.is_red_zone(x, y):
                print("[.] ", end="")
            else:
                print(" .  ", end="")

        def line_callback(x, y):
            print("")

        self.board.iter(cell_callback, line_callback)

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


def show_bitboard(width, height, bitboard):
    """
    ビットボード表示をするぜ☆（＾～＾）
    """

    def is_red_zone(x, y):
        """
        右上の足だけが踏めるマス。
        """

        address = (y*height)+(x % width)
        binary = 1 << address
        return (bitboard & binary) == binary

    calculator = Calculator(width, height)
    calculator.set_red_zone(is_red_zone)
    calculator.show_table()

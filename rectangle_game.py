from lib.calculator import Calculator


def is_red_zone(x, y):
    """
    右上の足だけが踏めるマス。
    """

    return x == y


calculator = Calculator(is_red_zone, 19, 19)
calculator.show_table()
calculator.calculate()
calculator.show_report()

print("Info    : Finished.")

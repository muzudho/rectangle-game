from lib.calculator import Calculator


def is_red_zone(x, y):
    """
    右上の足だけが踏めるマス。
    """

    return x == y


calculator = Calculator(19, 19)
calculator.set_red_zone(is_red_zone)
calculator.show_table()
calculator.calculate()
calculator.show_report()

print("Info    : Finished.")

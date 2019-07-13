from lib.calculator import Calculator

# Settings.
width = 19
height = 19


def is_red_zone(x, y):
    """
    右上の足だけが踏めるマス。
    """

    return x == y


calculator = Calculator(width, height)
calculator.set_red_zone(is_red_zone)
calculator.show_table()
calculator.calculate()
calculator.show_report()

print("Info    : Finished.")

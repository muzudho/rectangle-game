from lib.calculator import Calculator


def is_red_zone(x, y):
    """
    右上の足だけが踏めるマス。
    """

    """
    if(x == y):
        return True
    else:
        return False
    """

    # 1辺10を1区画と考えて４分割してみたときの、対角線上にある区画。
    x3 = x // 10
    y3 = y // 10
    if(x3 == y3):
        x2 = x % 10
        y2 = y % 10
        if 4 <= x2 and x2 <= 7 and 4 <= y2 and y2 <= 7:
            # ４分の１エリアの右上の区画。大外を除く。
            return True
        elif 2 <= x2 and x2 <= 3 and 2 <= y2 and y2 <= 3:
            # ４分の１エリアの左下の区画。
            return True
        elif x2 == 1 and y2 == 1:
            # ４分の１エリアの左下の区画。大外を除く。
            return True

    return False


calculator = Calculator(is_red_zone)
calculator.show_table()
calculator.calculate()

print("Info    : Finished.")

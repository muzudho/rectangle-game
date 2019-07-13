from lib.calculator import Calculator

width = 4
height = 4
num_of_states = 2 ** (width*height)
bitboard = 0


def is_red_zone(x, y):
    """
    右上の足だけが踏めるマス。
    """

    address = (y*height)+(x % width)
    binary = 1 << address
    return (bitboard & binary) == binary


calculator = Calculator(width, height)

best_sum = {"bitboard": 0, "succeed": 0, "failed": 0, "total": 0, "rate": 0}

for i in range(0, num_of_states):
    bitboard = i
    calculator.set_red_zone(is_red_zone)
    # print("#{}".format(bitboard))
    # calculator.show_table()
    calculator.calculate()
    sum = calculator.get_report_sum()
    if best_sum["rate"] < sum["rate"]:
        best_sum = {
            "bitboard": bitboard,
            "succeed": sum["succeed"],
            "failed": sum["failed"],
            "total": sum["total"],
            "rate": sum["rate"]
        }

print("Bitboard : {}".format(best_sum["bitboard"]))
print("Succeed  : {}".format(best_sum["succeed"]))
print("Failed   : {}".format(best_sum["failed"]))
print("total    : {}".format(best_sum["total"]))
print("Rate     : {:>.4f}".format(best_sum["rate"]))

print("Info     : Finished.")

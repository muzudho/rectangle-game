from lib.calculator import Calculator

bitboard = 0b0000000000000000


def is_red_zone(x, y):
    """
    右上の足だけが踏めるマス。
    """

    address = (y*4)+(x % 4)
    binary = 1 << address
    return (bitboard & binary) == binary


calculator = Calculator(4, 4)

best_sum = {"bitboard": 0, "succeed": 0, "failed": 0, "total": 0, "rate": 0}

for i in range(0, 65536):
    bitboard = i
    calculator.set_red_zone(is_red_zone)
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

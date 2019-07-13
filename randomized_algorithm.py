import random
from lib.calculator import Calculator

# Settings.
width = 5
height = 5
num_of_states = 2 ** (width*height)


def is_red_zone(x, y):
    """
    右上の足だけが踏めるマス。
    """

    address = (y*height)+(x % width)
    binary = 1 << address
    return (bitboard & binary) == binary


# Clear.
bitboard = 0
calculator = Calculator(width, height)
best_sum = {"bitboard": 0, "succeed": 0, "failed": 0, "total": 0, "rate": 0}

# 試行回数
try_count = 2 ** 16
if num_of_states < try_count:
    try_count = num_of_states

for i in range(0, try_count):
    if i % 5000 == 0:
        print("Progress: {}/{} ({:>3.0f}%)".format(i,
                                                   try_count, i/try_count*100))

    # Randomized algorithm.
    bitboard = random.randint(0, num_of_states-1)

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

# Result.
print("Bitboard : {}".format(best_sum["bitboard"]))
print("Succeed  : {}".format(best_sum["succeed"]))
print("Failed   : {}".format(best_sum["failed"]))
print("total    : {}".format(best_sum["total"]))
print("Rate     : {:>.4f}".format(best_sum["rate"]))

print("Info     : Finished.")

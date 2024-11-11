from convert import *


def gather_numbers() -> list[float]:
    nums = ""
    gather = []
    while nums != "done":
        nums = str(input("Type 'done' when finished. Enter a number: "))
        if str_to_float(nums) is not None:
            gather.append(str_to_float(nums))
    return gather
def main():
    print(gather_numbers())
main()


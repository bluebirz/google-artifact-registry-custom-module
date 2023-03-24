from my_modules.adder import my_sum


def do_adder():
    print(my_sum([1, 2]))
    print(my_sum([1, 2, 3]))
    print(my_sum([1, 2, 3, 4]))
    print(my_sum([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    do_adder()

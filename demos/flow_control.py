def break_at_5():
    i_range = range(0, 10)
    for i in i_range:
        if i == 5:
            break
        print(i)


def continue_at_5():
    i_range = range(0, 10)
    for i in i_range:
        if i == 5:
            continue
        print(i)


def multiple_return_points(a):
    if a == 0:
        return "a is 0"
    if a == 1:
        return "a is 1"


if __name__ == "__main__":
    # break_at_5()
    # continue_at_5()
    print(multiple_return_points(0))

    print(multiple_return_points(1))

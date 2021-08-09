def my_first_function():
    print("this is my first function")


def a_function_with_parameters(a, b):
    print(f"first parameter is: {a} second is: {b}")


def a_function_witch_returns(a, b):
    result = a + b
    return result


def a_function_with_multiple_returns(a, b):
    add = a + b
    subtract = a - b
    return add, subtract


if __name__ == "__main__":
    # comment
    # my_first_function()
    # print()

    # print("parameters")
    # c = 2
    # d = 1
    # a_function_with_parameters(c, d)
    # e = 2
    # f = 2
    # a_function_with_parameters(e, f)

    # a_function_with_parameters(4, 5)
    # print()

    # print("addition")
    # a, b = 2, 5
    # addition_result = a_function_witch_returns(a, b)
    # print(addition_result)
    # print()

    print("multiple returns")
    result_1, result_2 = a_function_with_multiple_returns(2, 1)
    print(f"result_1:{result_1}, result_2:{result_2}")
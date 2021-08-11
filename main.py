from read_problem import read_problem
from read_solution import read_solution, evaluate


if __name__ == "__main__":
    # paths = [
    #     "car-f-92.stu",
    #     "car-s-91.stu",
    #     "ear-f-83.stu",
    #     "hec-s-92.stu",
    #     "kfu-s-93.stu",
    #     "lse-f-91.stu",
    #     "pur-s-93.stu",
    #     "rye-s-93.stu",
    #     "sta-f-83.stu",
    #     "tre-s-92.stu",
    #     "uta-s-92.stu",
    #     "ute-s-92.stu",
    #     "yor-f-83.stu",
    # ]

    graph = read_problem("kfu-s-93.stu")
    solution = read_solution("kfu-s-93(12.90).sol")
    periods, feasible = evaluate(graph, solution)
    if feasible == True:
        print(f"solution uses {periods} periods")
    else:
        print("not feasible")
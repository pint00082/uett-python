from read_problem import read_problem
from read_solution import read_solution, evaluate
from save_solution import save_solution, color_dsatur

if __name__ == "__main__":
    paths = [
        "car-f-92.stu",
        "car-s-91.stu",
        "ear-f-83.stu",
        "hec-s-92.stu",
        "kfu-s-93.stu",
        "lse-f-91.stu",
        "pur-s-93.stu",
        "rye-s-93.stu",
        "sta-f-83.stu",
        "tre-s-92.stu",
        "uta-s-92.stu",
        "ute-s-92.stu",
        "yor-f-83.stu",
    ]

    # print("choose problem file")
    # for index, path in enumerate(paths):
    #     print(index, path)
    # i = input("Enter problem:")
    # problem = paths[int(i)]
    for problem in paths:
        graph = read_problem(problem)

        solution = color_dsatur(graph)
        periods, feasible = evaluate(graph, solution)
        if feasible == True:
            save_solution(problem, solution, periods)
            print(f"solution uses {periods} periods")

        else:
            print("not feasible")
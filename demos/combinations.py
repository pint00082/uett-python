from itertools import combinations

if __name__ == "__main__":
    a_list = [1, 2, 3, 4, 5]
    comb_2 = combinations(a_list, 2)
    for combination in comb_2:
        print(combination)
    print()

    comb_3 = combinations(a_list, 3)
    for combination in comb_3:
        print(combination)
    print()

    comb_4 = combinations(a_list, 4)
    for combination in comb_4:
        print(combination)
    print()

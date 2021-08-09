a_list = [1.2, "a", "b", 2, True]
print(a_list)
print()

# length
print("find length")
length = len(a_list)
print(length)
print()

# indexes
print("access with indexes")
print(a_list[0])
print(a_list[1])
print(a_list[2])
print(a_list[3])
print()

# iteration
print("access with iteration")
for position in a_list:
    print(position)
print()

# modify
a_list[2] = "newcomer"
print(a_list)

# contains
b_list = ["jo", "john", "mary"]
if "jo" in b_list:
    print("jo is in b_list")
else:
    print("jo is not in b_list")

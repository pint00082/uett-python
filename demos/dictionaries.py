a_dictionary = dict()
a_dictionary["key_a"] = "a"
a_dictionary[1] = "b"
a_dictionary[2] = 3
a_dictionary["rand"] = True
# key values
print()
print("access with key")
print(a_dictionary["key_a"])
print(a_dictionary[1])
print()
# warning upcoming error
print(a_dictionary[2])

# iteration keys
print("iteration keys")
for key in a_dictionary:
    print(key)
print()

# iteration values
print("iteration values")
for key in a_dictionary:
    print(a_dictionary[key])
print()

# modify
print(f"before modifications: {a_dictionary}")
a_dictionary[1] = 255
print(f"after modifications: {a_dictionary}")
print()

# keys()
print("keys")
print(a_dictionary.keys())
print()

# check keys
if "key_a" in a_dictionary.keys():
    print("key_a is a key")
else:
    print("key_a is not a key")

if "key_b" in a_dictionary.keys():
    print("key_b is a key")
else:
    print("key_b is not a key")

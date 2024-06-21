# dictionaries are mutable key-value pairs
# a = {}  # this is an empty dictionary
# b = set()  # this is an empty set
# print(a, type(a))
# print(b, type(b))

# we can strore key and values in a dictionary
dict1 = {"ramiz": 7,"noyem":1,"arif":2,"suro":54}
# print(dict1["ramiz"])
# print(dict1.keys())
# print(dict1.values())
# print(dict1["suro"])
# print(dict1.items())
# print(dict1)
# item assignment
dict1["lisan"] = 14
print(dict1)
print(dict1.get("lisan mondal")) # doesnt throw any error
# print(dict1["lisan mondal"]) # throws an error
dict1.pop("ramiz")
print(dict1)
# import pandas as p
# print(p.read_excel("miraz.xlsx"))
dict1["newkey"] = 3
print(dict1)
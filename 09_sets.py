# a set is a collection of well defined and unique elements
# sets are mutable
# sets do not support item indexing
# sets are always ordered
st = {2, 3, 4, 6, 7, 7, 7, 7, 8}
print(st)
st.add(1)
print(type(st))
st.remove(7)
print(st)
print(st.pop())  # removes and returns a random element from the set
# union and intersection of python sets
a1 = {1, 2, 2, 4, 5, 6}
a2 = {2, 3, 4, 5}
print(a1.union(a2))
print(a1.intersection(a2))

a3 = {4,5,1,2,7,9,6}
print(a3)
'''
sets are immutable and unordered collection of unique elements
'''
print(a3.pop())


# use "set" keyword to generate "set" data type
# set also can be generated with list

s1 = set([1, 2, 3, 4])
print(s1)

s2 = set("hello")

# characteristics
#1. No duplication
#2. no orders (unordered)

# tuple/list(ordered) <=> set(unordered) / dictionary
# => can not be indexed
# => want to index, then convert it into list/tuple

#usecase of set.
# intersect, union, subtraction
s3 = set([1, 2, 3, 4, 5, 6, 7])
s4 = set([5, 6, 7, 8, 9])

# intersection => 2 ways to do
print(s3 & s4)
print(s3.intersection(s4))

#union
print(s3 | s4)
print(s3.union(s4))

#difference
print(s3 - s4)
print(s3.difference(s4))

#changing element
# each functions "does not return" set data.

#single element
s3.add(99)
print(s3)

#multiple elements
s3.update([100, 101, 102])
print(s3)

#remove element
s3.remove(101)
print(s3)

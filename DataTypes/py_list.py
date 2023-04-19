#about list
odd = [1, 2, 3, 4, 5]
#list can be covered inside list => 2dimentional list
#elements inside list does not need to be same data type
#list can be empty when init
sample_list = ["a", "b", odd]
print(sample_list)

#indexing and slicing of index.

#indexing sample :
print(odd[2])

#slicing sample : exactally same with slicing in string array
#null point exception does not occur here.
print(odd[0:5])

#2dimentional list :
print(sample_list[2][2])

#calculating list also works same way.

#to get a length of a list works same way as string array
print(len(sample_list))
#also can be used like?
#however, the calling list occurs null pointer exception ( list index out of range)
print(len(sample_list[2]))

#replacing data in list
#1. replace with index
odd[2] = 9
print(odd[:])

#2. deleting element using del(), which is a Object level funtion ( calls from obj class?)
# every data type is a subclass of Obj class.
del odd[2]
print(odd[:])

#deleting also can be done with slicing

#internal functions in list
test_list = [0, 1, 2, 3, 4, 9, 6, 3, 2, 1]

#adding element inside list
test_list.append(10)
print(test_list)

#sorting list
#parameater of sort() function -> keyword-only parameater
#key = datatype , reverse = bool
test_list.sort(key=int, reverse=True)
print(test_list)

#if list includes different data types?
test_list.append(["a", "b"])
print(test_list)

#can not be used
#error occurs , becase if key=> list then int object is not iterable
#this is because of "implementation" problem. => using for loop for sorting
# print(test_list.sort(key = int , reverse = False ))

#s.extend(t) function : extends s with the "<contents> of target"
#string also can be used => same way as list,String array's content is "char" elements
test_list.extend("string")
print(test_list)

# if want to specify a index and insert, then use .insert(index ,element )
test_list.insert(0, "k")
print(test_list)

#reversed
#reverse() itself "does not return" anything.
# need to first reverse()
# and use it
test_list.reverse()
print(test_list)

# to get the index of element, use .index(element)
# if value is not in index, then error occurs.
print(test_list.index(10))

#removing element in list -> use .remove()
#removes the first <condition = true> element in the list
#remove function also does not returns value
print(test_list.remove("i"))

# using pop function in list -> parameater is "index" of element
# if parameater is null then, pops last index value.
print(test_list.pop())

# to generate stack/queue then use pop()/ pop(0) , insert(0,element)/ append()

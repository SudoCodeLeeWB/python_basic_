#Dictionary data type
# associative array / hash
# has a value of "key" and "value".
# gets the data not sequential but with key and value.

dic_data = {"name": "tom", "score": 4.5}

#adding dictionary pair inside dictionary
#index as "key" and element as value
dic_data["grade"] = "A+"
print(dic_data)

#using del function for deleting element inside dictionary
del dic_data["name"]
print(dic_data)

#what if the key does not exist in dictionary?
#error occurs.
#del dic_data["fake_key"]
print(dic_data)

#consider dictionary is same with list ,but the index is key.
#also dictionary is not suitable for slicing / indexing by number => only use "key"

#when considering key, the key must be immutable ( key value should not be changed)
#also, the dictionary should not have overlapping key value. elif it will ignore other data with same key. (when init, else it will just consider as changing the value of according key)

dic_data["grade"] = "B+"
print(dic_data)

#to get a value by key
#1. use a["key"] . this occurs error when key does not exist.
#2. use .get("key") function to get a value. this will return none when there is no key.
print(dic_data.get("fake_key", "default value"))

###internal functions of dictionary object.
#1. .keys()  generating a key object ( returns a list of keys as (dict_keys )
print(dic_data.keys())
#it returns key obj, not list.
#to convert obj -> list then use list() constructor
print(list(dic_data.keys()))

#to make values -> use .values
# this also returns dict_items obj. to convert into list then use list() constructor.
print(list(dic_data.values()))

# to get every items inside , use .items()
# this also returns dict_items obj
print(list(dic_data.items()))

#dictionary can not use append/insert/pop/remove/sort functions? -> look for implement
#cause "pop" is possible.
print(dic_data.pop("grade"))
print(dic_data)

#to search whether the key is inside of the dictionary
print('score' in dic_data)

#to erase every key-value pair, then use .clear()
print(dic_data.clear())

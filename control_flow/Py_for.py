class Py_for:

  def start(self, args):

    # for loop can be used in list/tuple/dictionary/
    # for loop can also used with "continue"
    # for loop is often used with range function.

    # list for loop sample
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = [(1, 2), (3, 4), (5, 6), (7, 8)]

    for var in sample_list:
      print(var)

    for (var1, var2) in sample_tuple:
      print(var1 + var2)

      #sample usecase
      # score dictionary which holds the student name and score => simply use tuple data type.
      # if use dictionary, then how to handle the key with value? (key - value 1:1 x)
      # filter the students who has more than 70 points.
    sample_tuple = [("john", 90), ("ted", 55), ("james", 60), ("alice", 75)]
    for (name, score) in sample_tuple:
      if score <= 70: continue
      # get the according key from row.
      print(name)

    # list comprehension : including for loop inside list obj ->for init in this case.
    # also can add condition ( if num%2 == 0 )
    result_list = [num * 3 for num in sample_list if num % 2 == 0]
    print(result_list)

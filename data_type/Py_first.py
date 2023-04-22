##input not generated


class Py_first:

  def start(self, args):
    #type casting
    country = str(3)
    city = int(3)
    # """
    # print('{1} is in {0}'.format(country, city))
    # print(country + ' is in ' + city)
    # print( '{0: .5f}' .format(1.0/3))
    # print('{0:*^12}'.format('fuxk'))

    # variables can change their type //  not declared with any particular type.

    # => want to specify then cast.

    # """
    # """
    # if type(country) != type(city) :
    #   print( country)
    #   print(type(country))
    # """

    # #REFER PEP FOR CLASS NAMING
    # #can get the type of a function by type()
    # #camel case for classes.
    # #CONSTANTS SHOULD BE ALL UPPER CASES
    # """
    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.
    # Example
    # """
    #words => list

    #파이썬 _ 기타흐름 제어 도구.

    #while statement
    #a,b = 0,1
    #while b < 10:
    #  print(a)
    #  a,b = a, a+b

    #if/ elif statement => replace switch/case
    x = int(input("please input number"))
    if x < 50:
      x = 50
      print("{} is not input num a")

    elif x == 50:
      print("value is : ")

#for loop : different from clang , which can control iteration and stop/break condition
    words = {'apple', 'banana', 'chocolate', 'delta', 'echo', 'whisky'}

    for w in words:
      print(w, len(w))

#it is difficult to manupliate collection while iterating. instead , make loop with copy of collection
#or create new collection
# => 이부분 collection 관련해서 다시 보기 .

# if need to iterate using sequence of numbers ,use range() 수열만들기. (0~)
    for i in range(5):
      print(i)


#combine range() and len()
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
      print(i, a[i])

  # => 루프 테크닉부터
  # https://docs.python.org/ko/3/tutorial/datastructures.html#tut-loopidioms
  # https://docs.python.org/ko/3/tutorial/controlflow.html
  # https://appmaster.io/ko/blog/10gaji-coegoyi-web-baegendeu-peureimweokeu#janggo
  # https://www.guru99.com/web-service-architecture.html
  # https://namu.wiki/w/Dart(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%20%EC%96%B8%EC%96%B4)

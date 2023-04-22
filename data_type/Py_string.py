#Data Types of PYTHON_1 String

## String is immutable


class Py_string:

  def start(self, args):
    # calculating string array => concatenation
    #1. concatenation
    head = " python "
    tail = "language"

    print(head + tail)

    #2. multiply
    # for repeating language
    equal = "="
    multi = head * 2

    print(equal * 50)
    print(multi)
    print(equal * 50)

    #3. getting the length of a string
    #empty space is counts for len()
    a = "ap ple"
    print(len(a))

    #4. indexing and slicing string
    b = "Life is too short, you need python"
    print(b[3])
    #index = > if stats from - then starts from back.
    print(b[-5])
    #slice does not include end number from end, ex) 0<= b <4
    print(b[0:4])
    #does not have null point exception,=> implemented in c for error handeling prints it until end
    print(b[6:180])
    #can also be empty for end pointer
    print(b[0:])
    #also can use - for slicing
    print(b[10:-40])
    #slicing Sample
    c = "20000907RainySunday"
    date = c[:8]
    weather = c[8:13]
    day = c[13:]

    print(date)
    print(weather)
    print(day)

    # String Formatting > when need to change the data in string (like placeholder)
    #1. using it as placeholder
    #int
    print("I have %d days left " % 3)
    #string
    print("I had %s for lunch " % "chicken")
    #as variable
    number_sample = 3
    #input variable => int
    print("I have %d days left " % number_sample)
    #does not care even the placeholder is for string data. ( auto convert?)
    print("I have %s days left " % number_sample)
    # """
    # format codes :
    # %s : string
    # %c : char
    # %d : int
    # %f : float
    # %o : octal
    # %x : hexadecimal
    # %% : LITERAL % itself

    # adding numbers inside placeholder indicates aligning it

    # """
    #using format method for formatting string
    #if entering multiple -> need to indicate the index of format
    #index also can be  name
    sample_name = "tom"
    sample_text = "I eat {var_sample}"
    print(sample_text.format(var_sample="apple"))

    #new type of formatting, with f formatting
    print(f"my name is {sample_name}")

    #string data type has its own methods
    #.count() function : returns number of specific charater in string
    print(sample_name.count("o"))

    #.find() function : returns the index of character in string array
    # if not exist, then returns -1
    print(sample_name.find("m"))

    # .index() function : returns the index of character in string array
    #if not exist, then Traceback occurs.
    print(sample_name.index("o"))

    #.join() function : insets specific parameater inside string.
    # join function can also be used in list/tuple
    print("_".join(sample_name))

    #upper/lower -> use to chage the case of string.
    #strip -> erase every empty space // lstrip rstrip for each side

    # replace(parameater1 , parameater2)
    # changes parameater1 -> parameater2
    print(sample_name.replace("tom", "jerry"))

    #split
    #default :  divides string array into chunks (to list) based on space
    #if indicates criterion (as a parameater) , use it.
    print(sample_text.split())

class Py_if:

  def start(self, args):

    money = False
    print(type(money))

    if money:
      print(money)
    else:
      print(money == True)  #trash code , why ! not supported?

#operators are same for python , returns bool data type , true/false
# """
# x<y
# x == y
# x != y
# x >= y
# x <= y

# operators can also be
# x or y  => || in java
# x and y => && in java
# not x => use !

# """

# sample2

    money = 3000
    if money >= 3000:
      print("ride taxi")
    else:
      print("walk")

    if money >= 3000 and money <= 5000:
      print("money between 3000 and 5000")
    else:
      print("over 5000 or less than 3000")
# """
# other operators
# in / not in

# usecase: ( in / not in object )
# object = > list/tuple/string array

# x in "obj"
# x not in "obj"

# """

    samp_tup = (2, 3, 4, 5, 6)
    if 3 in samp_tup:
      print("inside tuple")
    else:
      print("not in tuple")

##payment selection system sample
#dictionary for payment method and data => normally use payment_detail Obj

#later can be an function to call the payment method data from database (metadata) (using database api).
    saved_payment_method_data = {
      'visa_card': '3314 0453 0123 4563',
      'pay_point': 'point_account_number'
    }

    #this part also can be connected wtih front end to show the possible payment data that user has, for metadata
    selected_payment_method = input("type payment method")

    payment_method_list = ["visa_card", "cash", "pay_point"]

    if selected_payment_method in payment_method_list:
      payment_detail = saved_payment_method_data[selected_payment_method]
      print(payment_detail + " is your card number")
    else:
      print("payment failed")

# if want to do nothing in condition true/false condition, then use "pass"

# other use of if - else => use elif.
# same as switch / case in other languages.

# new example for payment :  with different payment methods
    saved_payment_method_data = {
      'pay_card': '3314 0453 0123 4563',
      'pay_point': 'point_account_number',
      'pay_cash': 'payment_code'
    }

    #this part also can be connected wtih front end to show the possible payment data that user has, for metadata

    selected_payment_method = input("type payment method // sample2")

    #this case, needs to hotcode the user input andd method list.
    # can the list can be a object that user created?
    #later TODO ==> after finishing the python basic, create a program

    payment_method_list = ["pay_card", "pay_cash", "pay_point"]

    print(selected_payment_method == payment_method_list[0])
    print(selected_payment_method == payment_method_list[1])
    print(selected_payment_method == payment_method_list[2])

    #differ cases
    if selected_payment_method == payment_method_list[0]:
      payment_detail = saved_payment_method_data[selected_payment_method]
      print(payment_detail + " is your card number")
    elif selected_payment_method == payment_method_list[1]:
      payment_detail = saved_payment_method_data[selected_payment_method]
      print(payment_detail + " is your payment code")
    else:
      print(payment_detail + "is your point account number")


# after looping with for study == TODO
##extend : is it possible to modify this code using for loop, without using elif?
# solution : use for loop in the range of list =>
# match the selected_payment_method with payment_method_list
# use the loop number as payment_method_list index number?
# or can use the "in" keyword for looping and match.

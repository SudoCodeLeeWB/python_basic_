# for repetive flow.


class Py_while:

  def start(self, args):

    count = 0
    while count < 10:
      count = count + 1
      print("count %d ", count)
      input_value = input("input break")
      if input_value == "break":
        break

    print("end of while loop")

    # print only odd number
    cnt = 0
    while cnt < 10:
      cnt = cnt + 1
      if cnt % 2 == 0: continue
      print(cnt)


#endless loop : use true / 1 in while condition.

def average(*numbers):
  # print(type(numbers))

   sum = 0
   for i in numbers:
    sum = sum + i
  #  print("average is:", sum / len(numbers))
  # return 7
   print("average is:", sum / len(numbers))

# average(4, 6)
# average(b=9)


c = average(5, 6, 7, 1)
print(c)
def name(**name):
  print(type(name))
  print("hello,", name["fname"], name["mname"], name["lname"])
  
name(mname="akash", lname="aniket", fname="kunal")

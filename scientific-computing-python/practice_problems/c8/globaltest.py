min = 7

def myfunc():
  global min
  if min == 7:
      min = 8

myfunc()

print("Python is ", min)

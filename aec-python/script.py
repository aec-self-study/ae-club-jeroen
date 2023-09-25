x = 2

print(x*2)

my_fruit_list = ['apple','banana']

for fruit in my_fruit_list:
    print(fruit)

def sq_int(x):
    y = x**2
    return y

y = 5
x = 4
def describe_evenness(x):
    if is_even(x):
        print( 'is even')
    elif is_odd(x):
        print( 'is odd')
    else:
        print( 'is not even or odd')

y = 5
x = 4

def is_even(x):
   if x % 2 == 0:
      return True
   else:
      return False

def is_odd(x):
   if x % 2 == 1:
      return True
   else:
      return False

def describe_evenness(x):
  if is_even(x):
    print("It’s even!")
  elif is_odd(x):
    print("It’s odd!")
  else:
    print("It’s neither even nor odd!")
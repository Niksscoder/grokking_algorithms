# Factorial
def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

#or lambda
fact = lambda x: 1 if x==1 else fact(x-1)*x 
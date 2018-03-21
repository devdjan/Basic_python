#To get the most out of this problem, try to figure out the answers by
# reading the code, not running it.
# Run the code only after you've used up a few of your checks.
def foo(x, y = 5):
    def bar(x):
        return x + 1
    return bar(y * 2)

foo(3)
# answer 11
# ----------------------
# Firstly  we have Gl.frame (foo - function(x,y)
# foo and variables x = 3, y = 5
# Next we execute def bar(x):
# Bar(x) - function. Foo is parent, bar inherits
# from foo(parent)
# Then we return bar(y * 2) = 10
#
#
# ----------------------
def foo(x, y = 5):
    def bar(x):
        return x + 1
    return bar( y * 2)

foo(3, 0)
# answer 1

# ----------------------
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)
# answer 5
# ----------------------

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)

# answer = 3
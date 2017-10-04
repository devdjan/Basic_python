#difference between staticmethod and class method
# foo, class_foo and static_foo

# class A(object):
#     def foo(self):
#         print("executing foo %s, %s" %(self,x))
#
#         def class_foo(cls ,x):
#             print("executing class_foo %s %s" %(cls,x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo %s" %x)
#
# a = A()
#
# a.foo(1)

#-------------------------------------------------------------------

#classmethod must have a reference to a class object as the first #
# parameter, whereas staticmethod can have no parameters at all.

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
#Here we have __init__, a typical initializer of Python class instances,
# which receives arguments as a typical instancemethod, having the first
#non-optional argument (self) that holds reference to a newly created instance.
    def from_string(selfcls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1
date2 = Date.from_string('11-00-2012')

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split("-"))
        return day <= 31 and month <=12 and year <= 3999
# So we do not have any access to what the class it is a function
# called syntactically like a method, but without access to the object and it's
# fields and another methods
    # usage
    is_date = Date.is_date_valid("11-09-2017")

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return "{0}-{1}-{2}". format(self.month, self.day, self.year)

    @staticmethod
    def millenium(month, day):
        return Date(month, day, 2000)

new_year = Date(1, 1, 2013)
millenium_new_year = Date.millenium(1, 2) #Also creates a Date new Object

new_year.display() #1-1-2013
millenium_new_year.display() #1-1-2000

print(isinstance(new_year, Date)) # True
print(isinstance(millenium_new_year, Date)) # True
# So, they both are instances of Data class. Экземпляры класса "дата"
# Но если посмотреть, то все "захардкожено" для создания Data objects
# Это значит если длаже Data class является подклассом, то подкласс
# все-ровно может создавать простой объект класс Data(без свойств подкласса)

# Example below.
class DateTime(Date):
    def display(self):
        return "{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year)

datetime1 = DateTime(10,10,1234)
datetime2 = DateTime.millenium(10 ,10)

# print(datetime2)  / <__main__.Date object at 0x0000006652B483C8>
# print(datetime1)  / <__main__.DateTime object at 0x0000006652B48390>

print(isinstance(datetime1, DateTime))
print(isinstance(datetime2, DateTime))

print(datetime1.display())
# returns "10-10-1990 - 00:00:00PM"
print(datetime2.display())
# returns "10-10-2000" because it's not a DateTime object but a Date object.
# Check the implementation of the millenium method on the Date class

# datetime2 != instatnce of Datetime.
# that's beacuse we are using @staticmethod DECORATOR
# In most cases this is undesired.
#
@classmethod
def millenium(cls, month, day):
    return cls(month, day, 2000)
# ensures that the class is not hard-coded but rather learnt.
# cls can be any subclass.
# The resulting object will rightly be an instance of cls.
# Let's test that out.
datetime_1 = DateTime(10,10, 1990)
datetime_2 = DateTime.millenium(10,10)

print(isinstance(datetime_1, DateTime))
print(isinstance(datetime_2, DateTime))

print(datetime_1.display())
print(datetime_2.display())

# Public, Private, Protected
# Public variable is normal variable
# Protected variable Single underscore _prefix
# Private variable is to add a double underscore __prefix
# Access Private variable outside class then used Syntax - _object._class__variable

class Employee:
    var1 = 2  # Public
    _var2 = 4  # Protected
    __var3 = 21  # Private - Not access outside of class

    def defs(self):
        print(self.__var3)

hr = Employee()
print(hr.var1)
print(hr._var2)
print(hr._Employee__var3)  # When we access Private variable outside class then this format will use

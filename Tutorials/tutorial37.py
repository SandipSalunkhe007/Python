# Multilevel Inheritance
class Dad:
    basketball = 1
class Son(Dad):
    dance = 5
    def isdance(self):
        return f'Yes I dance {self.dance}'

class Grandson(Son):
    dance = 8


darry = Dad()
larry = Son()
harry = Grandson()
print(harry.isdance())
print(harry.dance)  # Output -> 8 If dance present in first class then it will not check child class
print(larry.dance)  # Output -> 5
# Diamond shape problem
#             A
#             |
#         ---------
#        /         \
#       B           C
#        \         /
#         ---------
#             |
#             D
class A:
    def mat(self):
        print("This is the from class A")

class B(A):
    def mat(self):
        print("This is the from class B")

class C(A):
    def mat(self):
        print("This is the from class C")

class D(B, C):
    def mat(self):
        print("This is the from class D")

a = A()
b = B()
c = C()
d = D()

d.mat()
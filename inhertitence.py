class operation:
    def sum(self,n1,n2):
        z=n1+n2
        print("sum =",z)
    def sub(self,n1,n2):
        x=n1-n2
        print("sum =",x)
class operation2(operation):
 # def sum(self,n1,n2):

   ##    z = n1 + n2
     #   print("sum =", z)

#    def sub(self, n1, n2):
 #       x = n1 - n2
  #      print("sum =", x)

 def mul(self, n1, n2):
     y = n1 * n2
     print("sum =", y)


def main():
    op=operation2()
    op.mul(5,20)
    op.sum(5, 20)
    op.sub(5,20)
if __name__ == '__main__':main()

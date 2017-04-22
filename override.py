class operation:
    def sum(self,n1,n2):
        z=n1+n2
        print("sum =",z)
    def sub(self,n1,n2):
        x=n1-n2
        print("sub =",x)
class operation2(operation):
 # def sum(self,n1,n2):

   ##    z = n1 + n2
     #   print("sum =", z)

#    def sub(self, n1, n2):
 #       x = n1 - n2
  #      print("sum =", x)

 def mul(self, n1, n2):
     y = n1 * n2
     print("mul =", y)

 def sub(self, n1, n2):
     super().sub(n1,n2)
     
     #x = n1 - n2+10
     #print("sub =", x)


def main():
    op1=operation()
    op1.sub(50,20)

    op=operation2()
    op.mul(5,20)
    op.sum(5, 20)
    op.sub(50,20)
if __name__ == '__main__':main()

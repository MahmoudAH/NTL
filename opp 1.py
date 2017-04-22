#class car:
 #def mycar(self,name)
#       print("name is ",name)
#def main():
 # cars=car() #instance to copy the class car to the instance cars
 # cars.mycar("mahmoud ali hussein")    #= cars.mycar(cars) but python understand that so nor send "cars"



#3#if __name__ == '__main__':main()

 #class car:
 #   def mycar(self,n1,n2):
 #       z=n1*n2
 #       print(z)
##   cars = car()  # instance to copy the class car to the instance cars
  #  cars.mycar(5,4)# = cars.mycar(cars) but python understand that so nor send "cars"
#
  #  car1 = car()  # instance to copy the class car to the instance cars
 #   car1.mycar(8,4)# = cars.mycar(cars) but python understand that so nor send "cars"


#if __name__ == '__main__': main()



class car:
    def get(self):
       print("name is ",self._name)

    def set(self, name):

         self._name=name



def main():

  cars=car()                             #instance to copy the class car to the instance cars
  cars.set("mahmoud ali hussein")
  cars.get()                                 #= cars.mycar(cars) but python understand that so nor send "cars"#

  car1=car()
  car1.set("cdsaasd")
  car1.get()


if __name__ == '__main__': main()



























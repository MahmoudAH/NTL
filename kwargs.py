class car:
   # def __init__(self):
    ##   print("lkjdgf")
    def __init__(self,**kwargs):
        self.data =kwargs

    def get(self):
       print("name is ",self.data["name"])
       print("age  ",self.data["age"])
     #  print("value is ",self.data["value"])

# def set(self, name):
   def set_age(self,age):
      self.data["age"]=age
   def get_age(self):
       print(self.data["age"])


def main():

  cars=car(name="ahmed",age="21")
  # cars.set("mahmoud ali hussein")
  cars.get()
  car1=car(name="amr", value="554")
  #car1.set("cdsaasd")
  car1.get()


if __name__ == '__main__': main()





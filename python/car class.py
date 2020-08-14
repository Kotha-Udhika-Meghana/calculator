class CAR():
    def __init__(self,model,speed,price):
            self.model=model
            self.speed=speed
            self.price=price
    def display(self):
        print("model:",self.model)
        print("speed:",self.speed)
        print("price:",self.price)
class firing():
    def __init__(self,model,speed,price,num_of_bullets):
        CAR.__init__(self,model,speed,price)
        self.num_of_bullets=num_of_bullets
    def display(self):
        CAR.display(self)
        print("num_of_bullets:",self.num_of_bullets)
model=input("enter model name:")
speed=input("enter speed:")
price=input("enter price:")
num_of_bullets=input("enter num_of_bullets:")
c=firing(model,speed,price,num_of_bullets)
c.display()
        
class Car(object):
    price=10000       #class memeber
    def __init__(self,c):   #constructor
        self.color = c   #member belong to class object
def main():
    car1 = Car("Red")
    car2 = Car("Blue")
    print(car1.color, Car.price)

    ######修改类的属性
    Car.price = 9999

    ######动态增加类的属性
    Car.name='QQ'
    car1.

main()

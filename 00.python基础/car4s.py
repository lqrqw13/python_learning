class CarStore(object):
    def __init__(self):
        self.factory = Factory()
    def order(self,car_type):
        return self.factory.select_car_by_type(car_type)

class Factory(object):
    def select_car_by_type(self,car_type):
        if car_type =='伊兰特':
            return Elantra()
        else car_type == '索纳塔':
            return Sonata()

class Car(object):
    def move(self):
        print('车在跑')

class Elantra(Car):
    def __init__(self,name):
        self.name = name
        print(self.name)
class Sonata(Car):
    pass

car_store = CarStore()
car = car_store.order('伊兰特')

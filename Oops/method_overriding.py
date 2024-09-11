
from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Swift(Car):

    def start(self):
        print("swift start method")

    def accelerate(self):
        print("swift accelarte method")

    def stop(self):
        
        print("swift stop method")

    
car_instance=Swift()

car_instance.start()

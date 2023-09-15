from abc import ABC, abstractmethod

class Driver():
    def __init__(self, origin, destination, phone_number):
        self.phone_number = phone_number
        self.trip = (origin, destination)

    def publish_trip(self, app):
        app.offer_trip(self)

class Passenger():
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def find_driver(self, app):
        return app.find_trip(self.origin, self.destination)

class Carshare(ABC):
    @abstractmethod
    def offer_trip(self):
        pass

    @abstractmethod
    def find_trip(self):
        pass

class CarshareApp(Carshare):
    def __init__(self, name):
        self.__trips = []
        self.__name = name

    def offer_trip(self, driver):
        self.__trips.append(driver)

    def find_trip(self, desired_origin, desired_destination):
        for driver in self.__trips:
            if driver.trip[0] == desired_origin and driver.trip[1] == desired_destination:
                return driver.phone_number
        return "No available trips cover that route."

if __name__ == '__main__':
    blablacar = CarshareApp("Blablacar")
    paco = Driver("Jerez", "Madrid", "666 123 456")
    paco.publish_trip(blablacar)
    rafa = Driver("Barcelona", "Madrid", "678 123 459")
    rafa.publish_trip(blablacar)
    pepito = Passenger("Barcelona", "Madrid")
    print(pepito.find_driver(blablacar))


from abc import ABC, abstractmethod

class Television(ABC):  # ProductA
    @abstractmethod
    def television_function(self):
        pass

class SonyTelevision(Television):  # ProductA1
    def television_function(self):
        return "Sony Bravia Television Function"

class SamsungTelevision(Television):  # ProductA2
    def television_function(self):
        return "Samsung Television Function"

class Tablet(ABC):  # ProductB
    @abstractmethod
    def tablet_function(self):
        pass

class SonyTablet(Tablet):  # ProductB1
    def tablet_function(self):
        return "Sony Xperia Tablet Function"

class SamsungTablet(Tablet):  # ProductB2
    def tablet_function(self):
        return "Samsung Galaxy Tablet Function"

class Client:
    def client_code(self, factory):
        television = factory.create_television()
        tablet = factory.create_tablet()

        print(television.television_function())
        print(tablet.tablet_function())

class Factory(ABC):  # AbstractFactory
    @abstractmethod
    def create_television(self):
        pass

    @abstractmethod
    def create_tablet(self):
        pass

class SonyFactory(Factory):  # ConcreteFactory1
    def create_television(self):
        return SonyTelevision()

    def create_tablet(self):
        return SonyTablet()

class SamsungFactory(Factory):  # ConcreteFactory2
    def create_television(self):
        return SamsungTelevision()

    def create_tablet(self):
        return SamsungTablet()

if __name__ == "__main__":
    client = Client()
    print("Sony Factory: ")
    client.client_code(SonyFactory())
    print("\n")
    print("Samsung Factory: ")
    client.client_code(SamsungFactory())



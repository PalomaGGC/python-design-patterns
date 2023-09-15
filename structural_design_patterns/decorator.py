from abc import ABC, abstractmethod

class Coffee(ABC):
    def __init__(self) -> None:
        self._description = "Any coffee"

    def set_description(self, value: str) -> None:
        self._description = value

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def calculate_cost(self) -> float:
        raise NotImplementedError

class Frappuccino(Coffee):
    def __init__(self) -> None:
        self._description = "Frappuccino"

    def calculate_cost(self) -> float:
        return 1.99

class Latte(Coffee):
    def __init__(self) -> None:
        self._description = "Latte"

    def calculate_cost(self) -> float:
        return 1.85

# Define the decorators
class Extra(Coffee):
    @abstractmethod
    def get_description(self) -> str:
         raise NotImplementedError

    @abstractmethod
    def calculate_cost(self) -> str:
        raise NotImplementedError

class WhippedCream(Extra):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, with whipped cream"

    def calculate_cost(self) -> float:
        return self._coffee.calculate_cost() + 1.0

class Milk(Extra):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, with milk"

    def calculate_cost(self) -> float:
        return self._coffee.calculate_cost() + 0.5

class IceCream(Extra):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, with ice cream"

    def calculate_cost(self) -> float:
        return self._coffee.calculate_cost() + 1.5

class Caramel(Extra):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def get_description(self) -> str:
        return f"{self._coffee.get_description()}, with caramel"

    def calculate_cost(self) -> float:
        return self._coffee.calculate_cost() + 0.65

# Define the main function that prints the type of beverage and its cost
def view_details(coffee: Coffee) -> None:
    print(f"{coffee.get_description()} costs {coffee.calculate_cost()}")

if __name__ == "__main__":
    coffee01 = Frappuccino()
    coffee01 = WhippedCream(coffee01)
    view_details(coffee01)


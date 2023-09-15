class EuropeanAppliance():

    def plug_in(self, plug):
        if plug.supply_220v() == "Supplying 220v":
            return "The appliance seems to be working"

class EuropeanPlug():

    def supply_220v(self):
        return "Supplying 220v"

class AmericanPlug():

    def supply_120v(self):
        return "Supplying 120v"

class Adapter120to220(EuropeanPlug):

    def __init__(self, american_plug):
        self._american_plug = american_plug

    def supply_220v(self):
        return self._american_plug.supply_120v()[:-4] + "220v"

if __name__ == '__main__':
    my_hairdryer = EuropeanAppliance()
    airbnb_plug = AmericanPlug()
    aliexpress_adapter = Adapter120to220(airbnb_plug)

    print(my_hairdryer.plug_in(aliexpress_adapter))

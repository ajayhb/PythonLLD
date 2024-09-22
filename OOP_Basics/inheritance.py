class Vehicle:
    def __init__(self, name, model) -> None:
        self.name = name
        self.model = model
    
    def get_vehicle_details(self):
        print(f"Car Name: {self.name} :: Model: {self.model}", end="")

# Single inheritance
class FuelCar(Vehicle):
    def __init__(self, name, model, engine) -> None:
        Vehicle.__init__(self, name, model)
        self.engine = engine
    
    def get_fuelcar_details(self):
        Vehicle.get_vehicle_details(self)
        print(f":: Engine: {self.engine}", end="")

# Multilevel inheritance  
class GasolineCar(FuelCar):
    def __init__(self, name, model, engine, gastankcapacity) -> None:
        FuelCar.__init__(self, name, model, engine)
        self.gastankcapacity = gastankcapacity

    def get_gastank_details(self):
        Vehicle.get_vehicle_details(self)
        print(f":: GastankCapacity: {self.gastankcapacity}", end="")

# Hierarchial Inheritance
class ElectricCar(Vehicle):
    def __init__(self, name, model, batteryCapacity) -> None:
        Vehicle.__init__(self, name, model)
        self.batteryCapacity = batteryCapacity

    def get_battery_details(self):
        Vehicle.get_vehicle_details(self)
        print(f":: BatteryCapacity: {self.batteryCapacity}", end="")

# Multiple Inheritance
class HybridCar(FuelCar, ElectricCar):
    def __init__(self, name, model, engine, batteryCapacity, mileage) -> None:
        FuelCar.__init__(self, name, model, engine)
        ElectricCar.__init__(self, name, model, batteryCapacity)
        self.mileage = mileage

    def get_mileage(self):
        FuelCar.get_fuelcar_details(self)
        ElectricCar.get_battery_details(self)
        print(f":: Mileage: {self.mileage}")
        print("\n")

def main():
    vehicle = Vehicle("Mahindra", "XUV 700")
    vehicle.get_vehicle_details()
    print("\n")

    fuelcar = FuelCar("Mahindra", "XUV 700", "Sexy Engine")
    fuelcar.get_fuelcar_details()
    print("\n")

    electricxuv = ElectricCar("Mahindra", "XUV 700", "EV 500")
    electricxuv.get_battery_details()
    print("\n")

    gascar = GasolineCar("Mahindra", "XUV 700", "Sexy Engine", "1000L")
    gascar.get_gastank_details()
    print("\n")

    hybridxuv = HybridCar("Mahindra", "XUV 700", "Less Sexy Engine", "EV 400", "Okayish")
    hybridxuv.get_mileage()

if __name__ == "__main__":
    main()




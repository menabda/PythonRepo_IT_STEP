import pytest
from vehicle import Vehicle, ElectricVehicle

def test_vehicle_fuel_up():
    vehicle = Vehicle("BMW", "M4", 2020)
    assert vehicle.fuel_up == "Gas tank is empty and can not move."

def test_vehicle_drive():
    vehicle = Vehicle("Merecedes", "Benz", 2023)
    assert vehicle.drive == "The Benz is now driving."

def test_electric_vehicle_charge():
    ev = ElectricVehicle("Tesla", "Model S", 2022)
    assert ev.charge == "The vehicle is now charged."

def test_electric_vehicle_fuel_up():
    ev = ElectricVehicle("Tesla", "Model S", 2022)
    assert ev.fuel_up == "This vehicle has no fuel tank!"

if __name__ == "__main__":
    pytest.main()
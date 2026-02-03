import datetime

class MotorBike:
    def __init__(self,gear,speed):
        self.gear = gear
        self.speed = speed

    def __repr__(self):
        return repr((self.gear,self.speed))

honda = MotorBike("Honda",100)
suzuki = MotorBike("Suzuki",200)

#print(honda) # ('Honda', 100)
#print(suzuki) # ('Suzuki', 200)
print(suzuki.__str__()) # ('Suzuki', 200)

today = datetime.datetime.today()

print(today) # 2026-02-03 18:18:21.826250
print(today.__repr__()) # datetime.datetime(2026, 2, 3, 18, 18, 21, 826250)
print(today.__str__())  # 2026-02-03 18:18:21.826250




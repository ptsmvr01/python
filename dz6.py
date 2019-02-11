
class TownCar:

    def go(self):
        print('Going straight')
    def turn(self):
        print('Turning right...')
    def stop(self):
        print('Shutting down near the house')
    def __init__(self, name, speed, color, is_police ):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police 
class SportsCar:

    def go(self):
        print('Going straight')
    def turn(self):
        print('Turning left...')
    def stop(self):
        print('Shutting down near the house')
    def __init__(self, name, speed, color, is_police ):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
class WorkCar:

    def go(self):
        print('Going straight')
    def turn(self):
        print('Turning left...')
    def stop(self):
        print('Shutting down near the house')
    def __init__(self, name, speed, color, is_police ):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
class PoliceCar:

    def go(self):
        print('Going straight')
    def turn(self):
        print('None')
    def stop(self):
        print('Stopping and waiting near the donuts shop')
    def __init__(self, name, speed, color, is_police ):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police


towncar = TownCar('Toyota Prius 2019 | ', '60km/h | ', 'White | ', 'Not a police car')
print(towncar.name, towncar.speed, towncar.color, towncar.is_police)
towncar.go()
towncar.turn()
towncar.stop()
print('--------------------------------------------------------------------------------')

sportscar = SportsCar('BMW 8-Series | ', '120km/h | ', 'Night Blue | ', 'Not a police car')
print(sportscar.name, sportscar.speed, sportscar.color, sportscar.is_police)
sportscar.go()
sportscar.turn()
sportscar.stop()
print('--------------------------------------------------------------------------------')

workcar = WorkCar('Ford Transit Custom | ', '50km/h | ', 'White | ', 'Not a police car')
print(workcar.name, workcar.speed, workcar.color, workcar.is_police)
workcar.go()
workcar.turn()
workcar.stop()
print('--------------------------------------------------------------------------------')

policecar = PoliceCar('Dodge Charger | ', '90km/h | ', 'White and Black | ', 'POLICE CAR')
print(policecar.name, policecar.speed, policecar.color, policecar.is_police)
policecar.go()
policecar.turn()
policecar.stop()


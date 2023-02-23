import random


class Rockets():
    def __init__(self, weight, asteroidsShield, rocketColour):
        self.weight = weight
        self.altitude = 0
        self.asteroidsShield = asteroidsShield
        self.hitByAsteroideProbabilityPercentage = 40
        self.rocketColour = rocketColour
        self.hitOrNotHit = False

    def rocket_flight_altitude(self):
        self.isHitChance = random.uniform(0, 100)
        if (self.isHitChance > self.hitByAsteroideProbabilityPercentage):
            print("\n", self.rocketColour, "Rocket was hit by asteroide! let`s check if the shield can withstand!")

            if (self.asteroidsShield < random.randrange(self.asteroidsShield * 2)):
                print("\n Your shield didn`t hold, the rocket crashed! \n")
                self.hitOrNotHit = True
            else:
                self.hitOrNotHit = False

            if (self.hitOrNotHit == False):
                self.altitude = random.randint(1 + self.weight, 100 + self.weight)
                self.altitude = self.altitude - self.weight
                print("\n", self.rocketColour,"rocket flight altitude", self.altitude, "\n")


rocketParams = {'*RED*': (10, 100),
                '*YELLOW*': (1, 10),
                '*BLACK*': (10, 10)
                }

for key, value in rocketParams.items():
    rocket = Rockets(*value, key)
    rocket.rocket_flight_altitude()

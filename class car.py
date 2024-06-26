class car:
    color = "white"
    wheel = 4
    speed = "298km/hr"
    sit = 4
    def start(self):
        print("car started")
bmw = car()
print(bmw)
ferrari = car()
ferrari.color = "blue"
print(ferrari.color)
bmw.start()
ferrari.start()
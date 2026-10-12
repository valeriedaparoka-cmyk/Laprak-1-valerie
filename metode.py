class Hero:
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputWonder):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.wonder  = inputWonder
        Hero.jumlah += 1

    def siapa(self):
        return f"{self.name} memiliki power {self.power}"

    def healthUp(self, up):
        self.health += up
        
    def gethealth(self):
        return self.health

hero1 = Hero("Spaidermen", 100, 10, 5)
hero2 = Hero("Aironmen", 200, 15, 0)

print(hero1.siapa())
hero1.wonder = 20
print(f"wonder {hero1.name} = {hero1.wonder}") 
print(f"Jumlah hero = {Hero.jumlah}")
hero1.healthUp(20)
print(f"Health {hero1.name} = {hero1.gethealth()}")
print(f"Health {hero2.name} = {hero2.gethealth()}")
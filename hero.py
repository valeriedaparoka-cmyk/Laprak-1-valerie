class Hero: 
    pass

hero_1 = Hero() 
hero_2 = Hero() 

hero_1.name = "Betmen"
hero_2.name = "Ninja"

hero_1.power = 200
hero_2.power = 150


print(hero_1.name)
print(hero_2.name)  
print(hero_1.__dict__)
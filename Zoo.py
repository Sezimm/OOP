class Zoo:
    def __init__(self):
        self.animal_1 = 'Tiger'
        self.animal_2 = 'Begemot'
        self.animal_3 = 'Jiraf'
        
z = Zoo()

z.animal_1 = 'Leo'
z.animal_4 = [z.animal_2, z.animal_3]
z.animal_3 = 'Zmeya'

print(z.animal_1)
print(z.animal_2)
print(z.animal_3)
print(z.animal_4)
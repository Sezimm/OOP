class Factory:
    def engine(self):
        return 'Двигатель создан'
    
    def bridge(self):
        return 'Ходовая часть создана'

f = Factory()
print(f.engine())
print(f.bridge())

class Toyota(Factory):
    def wheels(self):
        return "Колёса готовы"

    def windows(self):
        return "Стёкла готовы"

t = Toyota()
l = [t.engine(), t.bridge(), t.wheels(), t.windows()]
print(l)





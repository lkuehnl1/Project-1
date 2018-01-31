class Item(object):
    def __init__(self,name,attack,weight,price):
        self.name= name
        self.attack =attack
        self.weight = weight
        self.price = price

class Equipment(object):
    def __init__(self):
        self.items = {}
    def add_items(self, item):
        self.items[item.name]=item
    def __str__(self):
        out= '\t'.join('Name','Atk','Arm', 'lb', 'val')
        for item in self.items.values():
            out+= '\n' + '\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.weight, item.price]])
equipment=Equipment()
print("What would you like to do?\n 1.Check Inventory 2.Check Character 3.Equiptment 4. Quit")
y=input()
if y=='3':
    Equipment(Item('Sword')
    print(equipment)

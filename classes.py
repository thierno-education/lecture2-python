# Class example 1
class Point():
    def __init__(self, f_input, s_input):
        self.x = f_input
        self.y = s_input

p = Point(10, 30)

print(p.x)
print(p.y)

# Class example 2
class Stadium():
    def __init__(self, capacity):
        self.capacity = capacity
        self.booked_seats = []
    def add_person(self, name):
        if self.available_seats() == 0:
            return False
        self.booked_seats.append(name)
        return True
    def available_seats(self):
        return self.capacity - len(self.booked_seats)

stadium = Stadium(4)
liste = ["Neymar", "Messi", "Ronaldo", "Haaland", "Mbappé"]

for name in liste:
    if stadium.add_person(name):
        print(f"Seats availble for {name}.")
    else:
        print(f"No available seats for {name}.")    

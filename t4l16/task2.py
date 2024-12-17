class Turtle():
    x = 0
    y = 0
    s = 1

    def get_coord(self):
        print(self.x, self.y)

    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
        

    def go_left(self):
        self.x -= self.s


    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s >= 0:
            self.s -= 1
        else:
            print("Error, the speed can't drop any lower")

    def count_moves(self, x2,y2):
        return (x2 + y2) / self.s
    
leonardo = Turtle()
leonardo.get_coord()
leonardo.go_up()
leonardo.get_coord()
leonardo.go_down()
leonardo.get_coord()
leonardo.evolve()
print(leonardo.count_moves(4,6))

class point:
    x1=0
    y1=0
    x2=0
    y2=0
    def calculate_midpoint(self):
        c=(self.x1 + self.x2)/2
        d=(self.y1 + self.y2)/2
        print("mid point")
        print(c,d)


p1 = point()
p1.x1= 2
p1.y1= 3
p1.x2= 5
p1.y2= 8

p1.calculate_midpoint()

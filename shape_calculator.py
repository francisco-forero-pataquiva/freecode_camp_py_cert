class Rectangle:
    def __repr__(self):
        s = f'{self.name}(width={self.width}, height={self.height})'
        return s
    def __init__(self,width,height):
        self.name = "Rectangle"
        self.width = width
        self.height = height
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self,new_height):
        self.height = new_height
    def get_area(self): 
        area = self.width * self.height
        return area 
    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter 
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal 
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            error_string = "Too big for picture."
            return error_string
        else:
            string_figure = ""
            for _ in range(0,(self.height)):
                string_figure += f'{"*"*self.width}\n'
            return string_figure
        
    def get_amount_inside(self,shape):     
        amount_inside = int(self.get_area() / shape.get_area())
        return amount_inside





class Square(Rectangle):
    
    def __repr__(self):
        s = f'{self.name}(side={self.width})'
        return s
    
    def __init__(self,side):
        self.name = "Square"
        self.width = side
        self.height = side
        
    def set_side(self,side):
        self.width = side
        self.height = side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

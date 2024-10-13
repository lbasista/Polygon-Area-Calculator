class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height <= 50 and self.width <= 50:
            pic = ""
            pic += "*" * self.width + "\n"
            return pic * self.height
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width
        return self.width

    def set_height(self, height):
        self.width = height
        self.height = height
        return self.height

    def __str__(self):
        return f'Square(side={self.height})'

# Tworzenie obiektu prostokąta
rect = Rectangle(10, 5)
print(rect)  # Wyświetli prostokąt
print(f"Area: {rect.get_area()}")  # Oblicz i wyświetl pole
print(f"Perimeter: {rect.get_perimeter()}")  # Oblicz i wyświetl obwód
print(f"Diagonal: {rect.get_diagonal()}")  # Oblicz i wyświetl przekątną
print(rect.get_picture())  # Wyświetl obrazek prostokąta

# Tworzenie obiektu kwadratu
square = Square(7)
print(square)  # Wyświetli kwadrat
print(f"Area: {square.get_area()}")  # Oblicz i wyświetl pole
print(f"Perimeter: {square.get_perimeter()}")  # Oblicz i wyświetl obwód
print(f"Diagonal: {square.get_diagonal()}")  # Oblicz i wyświetl przekątną
print(square.get_picture())  # Wyświetl obrazek kwadratu

# Zmiana rozmiaru kwadratu
square.set_side(5)
print(square)  # Wyświetli nowy kwadrat
print(f"Area: {square.get_area()}")  # Oblicz i wyświetl nowe pole
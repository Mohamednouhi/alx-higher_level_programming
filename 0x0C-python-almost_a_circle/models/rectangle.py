from base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        return self.__width
    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError(f"width must be an integer we got {type(width)}")
        if width < 0:
            raise ValueError(f"{width} is not supossed to be  negative")
        self.__width = width
    def get_height(self):
        return self.__height
            
    def set_height(self, height):
            
        if not isinstance(height, int):
            raise TypeError(f" must be an integer we got {type(height)}")
        if height < 0:
            raise ValueError(f"{height} is not suposed to be negative")
        self.__height = height
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x
        if not isinstance(x, int):
            raise TypeError(f" must be an integer we got {type(x)}")
        if x < 0:
            raise ValueError(f"{x} is not suposed to be negative")
        self.__x = x
    def get_y(self):
        return self.__y

    def set_y(self, y):
        if not isinstance(y, int):
            raise TypeError(f"must be an integer we got {type(y)}")
        if y < 0:
            raise ValueError(f"{y} is not supposed to be negative")
        self.__y = y

    def area(self):
        return self.get_height() * self.get_width()

    
    def display(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def update(self, *args, **kwargs):
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.__width = args[1]
            if len(args) == 3:
                self.__height = args[2]
            if len(args) == 4:
                self.__x = args[3]
            if len(args) == 5:
                self.__y = args[4]
            if len(args) > 5:
                raise ValueError(print("too many arguements"))
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.set_width(value)
                if key == 'height':
                    self.set_height(value)

                if key == 'x':
                    self.set_x(value)
                if key == 'y':
                    self.set_y(value)
    def to_dictionary(self):
        return {"id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y}


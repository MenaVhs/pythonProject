class Color:
    def __init__(self, color):
        self.__color = color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, new_color):
        if isinstance(new_color, str):
            self.__color = new_color

    def __str__(self):
        return f'Color: [Color: {self.color}]'

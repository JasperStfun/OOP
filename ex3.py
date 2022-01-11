class CoordError(Exception):
    pass

class Image:
    def __init__(self, width, height, background = "_"):
        self.__background = background
        self.__pixels = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __checkCoord(self, coord):
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordError("Координаты должны быть двумерным кортежем")
        
        if not ( 0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            raise CoordError("Координаты выходят за пределы изображения")

    def __setitem__(self, coord, color):
        self.__checkCoord(coord)

        if color == self.__background:
            self.__pixels.pop(coord, None)
        else:
            self.__pixels[coord] = color
            self.__colors.add(color)
    
    def __getitem__(self, coord):
        self.__checkCoord(coord)
        return self.__pixels.get(coord, self.__background)




img = Image(20, 4)
img[1, 1] = "*"; img[2, 1] = "*"; img[3, 1] = "*"
for row in img:
    for pixel in row:
        print(pixel, sep=" ", end="")
    print()
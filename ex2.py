class Clock:
    __DAY = 86400
    def __init__(self, secs:int):
        if not isinstance(secs, int):
            raise ValueError('Секунды должны быть целыми числами')
        
        self.__secs = secs % self.__DAY
    
    def getFormatTime(self):
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24
        return f"{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}"
    
    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0"+str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")
        
        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")
        
        self.__secs += other.getSeconds()
        return self

    def __eq__(self, other):
        return self.__secs == other.getSeconds()

    def __nq__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")
        
        if item == "hour":
            return (self.__secs // 3600) % 24
        elif item == "min":
            return (self.__secs // 60) % 60
        elif item == "sec":
            return self.__secs % 60
        
        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ должен быть строкой')
        
        if not isinstance(value, int):
            raise ValueError("значение должно быть целым числом")
        
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24

        if key == "hour":
            self.__secs = s + 60 * m + value * 3600
        elif key == "min":
            self.__secs = s + 60 * value + h * 3600
        elif key == "sec":
            self.__secs = value + 60 * m + h * 3600





c1 = Clock(80000)
c2 = Clock(200)
c3 = Clock(300)

print(c1["hour"], c1["min"], c1["sec"])
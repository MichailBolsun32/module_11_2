from inspect import getmodule

class Figure:
    filled_ = True # закрашенный
    sides_count = 0
    def __init__(self, color, *new_sides):
        self._color = (255, 255, 255)
        self._sides = [1] * self.sides_count # инициализация списка сторон (по умолчпнию длина стороны равна 1)
        self._sides = self.set_sides(*new_sides)
        if all(0 <= value < 255 for value in color):
            self._color = list(color) # список цветов в формате RGB)

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if all(x > 0 for x in new_sides):
                return True
        return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = []
            for el in new_sides:
                self._sides.append(int(el))
        return self._sides

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color[0] = int(r)
            self._color[1] = int(g)
            self._color[2] = int(b)
            print('Цвет изменился')
        else:
            print('Цвет не PGB, изменение цвета не возможно')

    def get_color(self):
        return self._color

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)


# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).

def introspection_info(obj):
   infa_ = dict()
   metod_ = list()
   atrib_ = list()
   # взяли тип объкта > перевели в str > разбили строку на массив и взяли второй эл.,
   # убрав первый и 2-а последних символа для нужного формата вывода
   infa_['type'] = str(type(obj)).split(' ')[1][1:-2]

   for attr in dir(obj): # итерируем по всем методам и атрибутам
       if callable(getattr(obj, attr)): # возвращаем атрибут и проверяем на исполняемость
           metod_.append(attr)
       else:
           atrib_.append(attr)

   infa_['attributes'] = atrib_
   infa_['methods'] = metod_
   infa_['module'] = str(getmodule(obj)).split(' ')[1][1:-1]

   return infa_


print(introspection_info(Figure))

# Project 4. Developed by Arkhipova Anastasia 19704
import turtle as tr
import math as mth
import random


class Ufo:
    """Tne class describe UFO's"""
    def __init__(self, name, x, y, size, speed, color, count_pillars, count_lamps, pillars_down=True, show_name=False,
                 made_in='Russia', engine_grade='Turbo UFO'):
        """Initialization method"""
        self.__name = name
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.count_pillars = count_pillars
        self.count_lamps = count_lamps
        self.pillars_down = pillars_down
        self.show_name = show_name
        self.__made_in = made_in
        self.__engine_grade = engine_grade

    @property
    def engine_grade(self):
        """Property method"""
        return self.__engine_grade

    @engine_grade.setter
    def engine_grade(self, new_grade):
        """Set-method"""
        if new_grade == '':
            print('Марка двигателя не может быть пустой строкой')
        else:
            self.__engine_grade = new_grade

    @engine_grade.getter
    def engine_grade(self):
        """Get-method"""
        if self.__engine_grade == 'Turbo UFO':
            return 'По умолчанию'
        else:
            return self.__engine_grade

    @property
    def set_made_in(self, made_in):
        """Set-method"""
        countries = ['USA', 'Russia']
        if made_in in countries:
            self.__made_in = made_in
        else:
            self.__made_in = None

    @property
    def get_made_in(self):
        """Property-method"""
        return self.__made_in

    def set_name(self, name):
        """Set-method"""
        self.__name = name

    def get_name(self):
        """Get-method"""
        return self.__name

    def show(self):
        """The method paints the UFO"""
        if self.pillars_down:
            for i in range(self.count_pillars):
                lx = self.x - self.size / 2 + i * (self.size / (self.count_pillars - 1))
                tr.penup()
                tr.goto(self.x, self.y + self.size / 3)
                tr.pendown()
                tr.goto(lx, self.y - self.size / 6)

        tr.penup()
        tr.goto(self.x, self.y - self.size / 12)
        tr.pendown()
        tr.fillcolor('blue')
        tr.begin_fill()
        tr.circle(self.size / 4)
        tr.end_fill()

        tr.penup()
        tr.fillcolor(self.color)
        tr.goto(self.x - self.size / 2, self.y + self.size / 4)
        tr.pendown()
        tr.begin_fill()
        tr.forward(self.size)
        i = mth.pi / 2
        while i <= 3 * mth.pi / 2:
            sx = (self.size / 2) * mth.sin(i)
            sy = (self.size / 3) * mth.cos(i)
            tr.goto(self.x + sx, self.y + self.size / 4 + sy)
            i += mth.pi / self.size
        tr.end_fill()

        tr.fillcolor('yellow')
        n = self.count_lamps + 2
        for i in range(1, n - 1):
            dx = self.size / (n - 1)
            tr.begin_fill()
            tr.penup()
            tr.goto(self.x - self.size / 2 + i * dx, self.y + self.size / 14)
            tr.pendown()
            tr.circle(dx / 4)
            tr.end_fill()

        if self.show_name:
            tr.penup()
            tr.goto(self.x, self.y + self.size / 2)
            tr.write(self.__name, align='center')
            tr.pendown()

    def go_x(self, new_x):
        """The method calculates the new coordinate x"""
        self.x = self.x + (new_x * self.speed)

    def go_y(self, new_y):
        """The method calculates the new coordinate y"""
        self.y = self.y + (new_y * self.speed)

    def __str___(self):
        """String method"""
        if self.show_name:
            s = '\nСконструировано НЛО под названием ' + self.__name + '\n'
        else:
            s = '\nНазвание неизвестно' + '\n'

        s += 'Координаты (' + str(self.x) + ', ' + str(self.y) + ')\n'
        s += 'Размер: ' + str(self.size) + '\n'
        s += 'Цвет ' + self.color + '\n'
        s += str(self.count_pillars) + ' лап\n'
        s += str(self.count_lamps) + ' ламп\n'

        if self.pillars_down:
            s += 'Опоры опущены'
        else:
            s += 'Опоры подняты'
        return s

    def __repr__(self):
        """Report method"""
        return self.__str___()


tr.tracer(0)
tr.hideturtle()
COLORS = ['blue', 'purple', 'red', 'green', 'orange', 'yellow']
ufo1 = Ufo('Пришелец-1', 10, 200, 150, 10, COLORS[random.randint(0, len(COLORS) - 1)], 5, 6)
ufo2 = Ufo('Пришелец-2', 150, -150, 150, 5, COLORS[random.randint(0, len(COLORS) - 1)], 2, 4)
ufo3 = Ufo('Пришелец-3', -100, -150, 150, 8, COLORS[random.randint(0, len(COLORS) - 1)], 3, 3)
ufo4 = Ufo('Пришелец-4', -200, 200, 150, 3, COLORS[random.randint(0, len(COLORS) - 1)], 5, 2)
ufo5 = Ufo('Пришелец-5', 50, -150, 150, 1, COLORS[random.randint(0, len(COLORS) - 1)], 2, 3)
ufo_list = [ufo1, ufo2, ufo3, ufo4, ufo5]

while True:
    tr.clear()
    for ufo in range(0, len(ufo_list)):
        new_x = random.randint(-2, 2)
        new_y = random.randint(-2, 2)
        ufo_list[ufo].go_x(new_x)
        ufo_list[ufo].go_y(new_y)
        ufo_list[ufo].show()
    tr.update()
tr.done()

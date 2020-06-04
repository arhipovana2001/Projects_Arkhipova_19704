class Load:
    """Класс для загрузки и хранения данных"""
    table = []
    first_lessons = []
    second_lessons = []
    third_lessons = []
    fourth_lessons = []
    fifth_lessons = []

    @classmethod
    def write(cls, file_name):
        """Метод считывает данные из файла"""
        with open(file_name, encoding='utf-8') as inp_file:
            k = 0
            all_table = []
            for item in inp_file:
                if k == 0:
                    lst = str(item.split()[0])[:-1]
                    cls.number_of_group = lst
                    k = 1
                elif k != 0:
                    lst = item[:-1]
                    all_table.append(lst)
            index = {'Понедельник': None, 'Вторник': None, 'Среда': None,
                     'Четверг': None, 'Пятница': None, 'Суббота': None}
            for day in index.keys():
                index[day] = all_table.index(day)
            monday = all_table[index['Понедельник'] + 1:index['Вторник']]
            tuesday = all_table[index['Вторник'] + 1:index['Среда']]
            wednesday = all_table[index['Среда'] + 1:index['Четверг']]
            thursday = all_table[index['Четверг'] + 1:index['Пятница']]
            friday = all_table[index['Пятница'] + 1:index['Суббота']]
            saturday = all_table[index['Суббота'] + 1:]
            week = [monday, tuesday, wednesday, thursday, friday, saturday]
            week_new = []
            for day in week:
                time_lessons = ['09:00', '10:50', '12:40', '14:30', '16:20']
                for i in range(0, len(day)):
                    for time in range(0, len(time_lessons)):
                        c = day[i].split()
                        if time_lessons[time] in c:
                            time_lessons.pop(time)
                            time_lessons.insert(time, day[i])
                            break
                day = time_lessons
                week_new.append(day)
            for day in week_new:
                if len(day[0]) == 5:
                    cls.first_lessons.append([])
                else:
                    cls.first_lessons.append(day[0])
                if len(day[1]) == 5:
                    cls.second_lessons.append([])
                else:
                    cls.second_lessons.append(day[1])
                if len(day[2]) == 5:
                    cls.third_lessons.append([])
                else:
                    cls.third_lessons.append(day[2])
                if len(day[3]) == 5:
                    cls.fourth_lessons.append([])
                else:
                    cls.fourth_lessons.append(day[3])
                if len(day[4]) == 5:
                    cls.fifth_lessons.append([])
                else:
                    cls.fifth_lessons.append(day[4])
            cls.table.append(Lessons(*cls.first_lessons))
            cls.table.append(Lessons(*cls.second_lessons))
            cls.table.append(Lessons(*cls.third_lessons))
            cls.table.append(Lessons(*cls.fourth_lessons))
            cls.table.append(Lessons(*cls.fifth_lessons))


class Lessons:
    """Класс представляет занятия"""
    def __init__(self, monday, tuesday, wednesday, thursday, friday, saturday):
        """Метод инициализации"""
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday= thursday
        self.friday = friday
        self.saturday = saturday

    def __str__(self):
        """Метод строкового представления"""
        total = ''
        if not self.monday:
            total += ' ' * 5 + '-' * 5 + ' ' * 5 + '|'
        else:
            day = self.monday.split()
            les = ' '.join(day[2:])
            if len(les) > 15:
                total += les[:15] + '|'
            else:
                total += ' ' * int(((15 - len(les)) / 2)) + les + \
                         ' ' * int(((16 - len(les)) / 2)) + '|'

        if not self.tuesday:
            total += ' ' * 5 + '-' * 5 + ' ' * 5 + '|'
        else:
            day = self.tuesday.split()
            les = ' '.join(day[2:])
            if len(les) > 15:
                total += les[:15] + '|'
            else:
                total += ' ' * int(((15 - len(les)) / 2)) + les +\
                         ' ' * int(((16 - len(les)) / 2)) + '|'

        if not self.wednesday:
            total += ' ' * 5 + '-' * 5 + ' ' * 5 + '|'
        else:
            day = self.wednesday.split()
            les = ' '.join(day[2:])
            if len(les) > 15:
                total += les[:15] + '|'
            else:
                total += ' ' * int(((15 - len(les)) / 2)) + les +\
                         ' ' * int(((16 - len(les)) / 2)) + '|'

        if not self.thursday:
            total += ' ' * 5 + '-' * 5 + ' ' * 5 + '|'
        else:
            day = self.thursday.split()
            les = ' '.join(day[2:])
            if len(les) > 15:
                total += les[:15] + '|'
            else:
                total += ' ' * int(((15 - len(les)) / 2)) + les +\
                         ' ' * int(((16 - len(les)) / 2)) + '|'

        if not self.friday:
            total += ' ' * 5 + '-' * 5 + ' ' * 5 + '|'
        else:
            day = self.friday.split()
            les = ' '.join(day[2:])
            if len(les) > 15:
                total += les[:15] + '|'
            else:
                total += ' ' * int(((15 - len(les)) / 2)) + les +\
                         ' ' * int(((16 - len(les)) / 2)) + '|'

        if not self.saturday:
            total += ' ' * 5 + '-' * 5 + ' ' * 5 + '|'
        else:
            day = self.saturday.split()
            les = ' '.join(day[2:])
            if len(les) > 15:
                total += les[:15] + '|'
            else:
                total += ' ' * int(((15 - len(les)) / 2)) + les +\
                         ' ' * int(((16 - len(les)) / 2)) + '|'
        return total


lessons = Load.write('table.txt')
print('-' * 104)
print('|' + ' ' * 39 + 'THE GROUP SCHEDULE 19704' + ' ' * 39 + '|')
print('-' * 104)
print('| TIME |     MONDAY    |    TUESDAY    |   WEDNESDAY   |    THURSDAY   |     FRIDAY    |    SATURDAY   |')
print('-' * 104)
time_lessons = ['09:00', '10:50', '12:40', '14:30', '16:20']
for time, item in zip(time_lessons, Load.table):
    print('|' + time + ' |', end='')
    print(item)
    print('-' * 104)

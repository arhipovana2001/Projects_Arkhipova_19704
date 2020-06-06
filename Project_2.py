import time


class Load:
    """Класс для загрузки и хранения данных"""
    songs_lst = []

    @classmethod
    def write_songs(cls, fl_songs):
        """Метод позволяет считывать данные из файлов"""
        with open(fl_songs, encoding='utf-8') as inp_songs:
            for song in inp_songs:
                lst = song.split(';')
                cls.songs_lst.append(Song(*lst[:-1]))


class Album:
    """Класс представляет альбом"""
    all_songs = []

    def __init__(self):
        """Метод инициализации"""
        Album.all_songs = []

    def __str__(self):
        """Метод строкового представления"""
        return str(Album.all_songs)

    def add_song(self, song):
        """Метод добавляет товар в корзину"""
        if song not in Album.all_songs:
            Album.all_songs.append(song)
        else:
            print('Вы уже добавили эту песню в альбом.')

    def delete_song(self, song):
        """Метод удаляет товар из корзины"""
        if song in Album.all_songs:
            Album.all_songs.pop(Album.all_songs.index(song))
        else:
            print('Такой песни нет в альбоме.')

    def count_total_duration(self):
        """Метод позволяет посчитать общую продолжительность в секундах"""
        total = 0
        for song in Album.all_songs:
            if song.duration is None:
                return 'Невозможно посчитать'
            else:
                total += song.duration
        return total

    def count_total_number(self):
        """Метод позволяет посчитать общее кол-во песен в альбоме"""
        return len(Album.all_songs)


class Song:
    """Класс представляет песни"""

    def __init__(self, artist, name, album, year, duration):
        """Метод инициализации"""
        self.artist = str(artist)
        self.name = str(name)
        self.album = str(album)
        try:
            self.year = int(year)
        except ValueError:
            self.year = None
        try:
            self.__duration = int(duration)  # продолжительность песни
        except ValueError:
            self.__duration = None
        self.status = False
        self.pause_time = 0
        self.begin = 0  # время, когда песня начала играть

    def __str__(self):
        """Метод строкового представления"""
        total = ''
        total += 'Исполнитель: ' + str(self.artist) + '\n'
        total += 'Название: ' + str(self.name) + '\n'
        total += 'Альбом: ' + str(self.album) + '\n'
        if self.status is True:
            total += 'Воспроизведение: да' + '\n'
        elif self.status is False:
            total += 'Воспроизведение: нет' + '\n'
        return total

    def __repr__(self):
        """Метод - репорт"""
        total = str(self.artist) + ' - ' + str(self.name)
        return total

    def play(self):
        """Метод ставит песню на воспроизведение"""
        if self.status is True:
            return 'Воспроизведение уже идет'
        for item in Album.all_songs:
            if item.status is True:
                item.stop()
        self.status = True  # воспроизведение начато
        self.begin = time.time()  # сек когда песня начала играть
        return 'Воспроизведение начато'

    def stop(self):
        """Метод останавливает воспроизведение песни"""
        if self.status is False:
            return 'Песня была выключена ранее'
        else:
            self.status = False
            self.begin = 0
            return 'Воспроизведение остановлено'

    def pause(self):
        """Метод ставит песню на паузу"""
        pass

    def info(self):
        """Метод позволяет узнать, играет ли песня"""
        if (time.time() - self.begin) < self.__duration:
            print('Песня воспроизводится. ', end='')
            print(f'Осталось {int(self.__duration - (time.time() - self.begin))} сек.')
        else:
            print('Песня не воспроизводится')


Load.write_songs('songs.txt')
album1 = Album()
for item in Load.songs_lst:
    print(item)
    album1.add_song(item)
print(album1)
print()


def main():
    print('Основные команды:')
    print('1. Поставить песню на воспроизведение.')
    print('2. Остановить воспроизведение.')
    print('3. Показать информацию об альбоме.')
    print('4. Показать информацию о песне.')
    print('5. Узнать состояние песни.')

    def function1():
        print(Album.all_songs)
        print('Введите номер песни, которую нужно поставить на воспроизведение:')
        index = int(input())
        print(Album.all_songs[index - 1].play())

    def function2():
        print(Album.all_songs)
        print('Введите номер песни, которую нужно остановить:')
        index = int(input())
        print(Album.all_songs[index - 1].stop())

    def function3():
        print(Album.all_songs)

    def function4():
        print(Album.all_songs)
        print('Введите номер песни, информацию о которой нужно вывести:')
        index = int(input())
        print(Album.all_songs[index - 1])

    def function5():
        print(Album.all_songs)
        print('Введите номер песни, информацию о которой нужно вывести:')
        index = int(input())
        Album.all_songs[index - 1].info()

    while True:
        print('Введите номер команды:')
        menu = int(input())
        if menu == 1:
            function1()
        elif menu == 2:
            function2()
        elif menu == 3:
            function3()
        elif menu == 4:
            function4()
        elif menu == 5:
            function5()
        else:
            print('Работа программы завершена.')
            exit()


main()

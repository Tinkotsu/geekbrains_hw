class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручечкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашиком')


class Handle(Stationery):
    def draw(self):
        print('Рисуем фломиком')


pen = Pen('ручечка')
pencil = Pencil('карандашик')
handle = Handle('маркер')
stat = Stationery('штучка')

stat.draw()
pen.draw()
pencil.draw()
handle.draw()

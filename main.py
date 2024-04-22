# Створіть імітаційну модель «Причал морських катерів».
# Введіть таку інформацію:
# 1. Середній час між появою пасажирів на причалі у різний
# час доби;
# 2. Середній час між появою катерів на причалі у різний час
# доби;
# 3. Тип зупинки катера (кінцева або інша).

# Визначіть:
# 1. Середній час перебування людини на зупинці;
# 2. Достатній інтервал часу між приходами катерів, коли на
# зупинці не більше N людей одночасно;
# 3. Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно.


from queue import PriorityQueue


class Port:
    def __init__(self):
        self.queue = PriorityQueue()

    def add_ship(self, stop, time, priority):
        self.queue.put((priority, stop, time))

    def handle_race(self):
        if self.queue.empty():
            print("There is no races")
            return

        priority, stop, time = self.queue.get()

        print(f'{priority}, {stop}, {time}')


solver = Port()

solver.add_ship('Other', "20:32", 2)
solver.add_ship('Final', "12:21", 3)
solver.add_ship('Other', "17:15", 1)

solver.handle_race()
solver.handle_race()
solver.handle_race()
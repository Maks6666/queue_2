# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.


from queue import PriorityQueue

class WebSite:
    def __init__(self):
        self.queue = PriorityQueue()

    def add_user(self, user, time, priority):
        self.queue.put((priority, user, time))


    def show(self):
        if not self.queue.empty():
            for priority, data, time in self.queue.queue:
                print(f"Priority: {priority}, username: {data}, time: {time}")
        else:
            return False

user1 = WebSite()
user1.add_user("A", "12:00", 5)

user2 = WebSite()
user1.add_user("B", "13:00", 3)

user1.show()
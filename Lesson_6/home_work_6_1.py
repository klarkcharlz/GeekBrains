# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import random
import time

""" Версия без контроля переключения режимов"""
class TrafficLight:
    """Класс светофора
    color_dict - Словарь с продолжительностью зажигания каждого цвета
     __color - Приватная переменная содержащая информацию о текущем цвете
    """
    color_dict = {"RED":7 , "YELLOW":2, "GREEN":5}
    __color = None

    def timer(self, interval:int):
        """Функция ведет отсчет до момента следующего переключения цвета"""
        while interval > 0:
            print(f"Осталось {interval} секунд.")
            time.sleep(1)
            interval -= 1

    def running(self):
        """Функция запускает бесконечную работу светофора"""
        while True:
            for key in self.color_dict:
                self.__color = self.color_dict[key]
                print(f"Сейчас загорится {key} цвет.")
                self.timer(self.__color)

traffic_lights = TrafficLight()  # создаем экземпляр класса
traffic_lights.running()  # включаем светофор


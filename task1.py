import time

class TrafficLight:
    __color = ''

    def running(self):
        while True:
            TrafficLight.__color = "\033[31mкрасный"
            print(TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color = '\033[31mкрасный \033[37m+ \033[33mжёлтый'
            print(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = '\033[32mзелёный'
            print(TrafficLight.__color)
            time.sleep(5)
            TrafficLight.__color = '\033[33mжёлтый'
            print(TrafficLight.__color)
            time.sleep(2)

a = TrafficLight()
a.running()
import time


class TrafficLight:
    def __init__(self):
        self._color = None

    def running(self):
        mods = ['red', 'yellow', 'green']
        for mod in mods:
            self._color = mod
            print(self._color)
            if mod == 'red':
                time.sleep(7)
            elif mod == 'yellow':
                time.sleep(2)
            elif mod == 'green':
                time.sleep(5)


tl = TrafficLight()
tl.running()
print('done')

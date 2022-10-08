class Road:
    _length = 0
    _width = 0
    def calc(self, l, w, m, h):
        Road._length = l
        Road._width = w
        self.massa = m
        self.hide = h
        res = float(Road._length * Road._width * self.massa * self.hide)
        if res > 1000:
            return str(res / 1000) + ' т.'
        else:
            return str(res) + ' кг.'
a = Road()
print(a.calc(5000, 20, 25, 5))
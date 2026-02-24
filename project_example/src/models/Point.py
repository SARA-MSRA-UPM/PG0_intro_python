
class Point(object):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}, Z: {self.z}"
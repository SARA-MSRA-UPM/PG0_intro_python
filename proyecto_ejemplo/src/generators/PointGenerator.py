from random import Random
from ..models.Point import Point

class PointGenerator:
    def __init__(self, seed: int = 33):
        self.seed = seed
        self.random = Random(x=self.seed)

    def random_point(self) -> Point:
        return Point(
            x=self.random.randint(0, 100),
            y=self.random.randint(0, 100),
            z=self.random.randint(0, 100)
        )
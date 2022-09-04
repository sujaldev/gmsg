class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def xy(self):
        return self.x, self.y

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

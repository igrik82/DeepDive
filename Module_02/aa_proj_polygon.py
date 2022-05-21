"""Class Polygon"""
from cmath import pi
import math


class Polygon:
    """Class Poligon"""

    def __init__(self, edges: int, circumradius: int) -> None:
        self.edges = edges
        self.circumradius = circumradius
        self.cache = {}

    @property
    def edges(self) -> int:
        """Get edges"""
        return self._edges

    @edges.setter
    def edges(self, value: int) -> int:
        """Set edges"""
        if not isinstance(value, int):
            raise ValueError("Only integer allowed!")
        elif value < 3:
            raise ValueError("At least 3 edges must be provided")
        else:
            self._edges = value

    @property
    def circumradius(self) -> int:
        """Get circumradius"""
        return self._circumradius

    @circumradius.setter
    def circumradius(self, value: int) -> int:
        """Set circumradius"""
        if not isinstance(value, int):
            raise ValueError("Only integer allowed!")

        self._circumradius = value

    @property
    def apothem(self):
        """Get apothem"""

        # Caching calculated rezult
        # Make dictionary thith tuple key
        if ("apothem", self.edges, self.circumradius) not in self.cache:
            # print("Calcutating...")
            self.cache[("apothem", self.edges, self.circumradius)] = round(
                self.circumradius * math.cos(pi / self.edges), 2
            )

        return self.cache[("apothem", self.edges, self.circumradius)]

    @property
    def length(self):
        """Get lenght"""

        # Cahing calculated rezult
        if ("length", self.edges, self.circumradius) not in self.cache:
            # print("Calculating...")
            self.cache[("length", self.edges, self.circumradius)] = round(
                2 * self.circumradius * math.sin(pi / self.edges), 2
            )

        return self.cache[("length", self.edges, self.circumradius)]

    @property
    def area(self):
        """Get area"""

        return round((1 / 2) * self.edges * self.length * self.apothem, 2)

    @property
    def perimeter(self):
        """Get perimetr"""

        return self.edges * self.length

    @property
    def interior_angle(self):
        """Get interior angle"""

        return round((self.edges - 2) * 180 / self.edges, 2)

    def __repr__(self) -> str:
        return f"Polygon obj edges={self.edges}, circumradius={self.circumradius},\
apothem={self.apothem}, length={self.length}, area={self.area},\
perimetr={self.perimeter}, interior angle={self.interior_angle}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return (self.edges, self.circumradius) == (other.edges, self.circumradius)

        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.edges > other.edges

        return NotImplemented


class Polygons:
    """Polygons sequens type"""

    def __init__(self, num_vertices: int, circumradius: int) -> object:
        if num_vertices < 3:
            raise ValueError("Must be at least 3")
        self._m = num_vertices
        self.circumradius = circumradius
        self._polygons = [Polygon(i, self.circumradius) for i in range(3, self._m + 1)]

    def __len__(self):
        return len(self._polygons)

    def __repr__(self) -> str:
        return f"Class Polygons with {len(self)} polygons"

    def __getitem__(self, number):
        return self._polygons[number]

    @property
    def max_efficiency(self):
        """Get max efficency poligon"""
        max_eff = sorted(self._polygons, key=lambda pol: pol.area / pol.perimeter, reverse=True)
        return max_eff[0], max_eff[0].area / max_eff[0].perimeter


poligons1 = Polygons(8, 9)
print(poligons1.max_efficiency)

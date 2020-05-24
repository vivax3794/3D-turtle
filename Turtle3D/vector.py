from dataclasses import dataclass
from math import sin, cos


@dataclass
class Vector3:
    """
    A 3d vector.
    """
    x: float
    y: float
    z: float

    def to_2d(self) -> "Vector2":
        """
        Convert this vector into a 2d vector.
        """
        a = self
        c = Vector3(0, 10, 10)
        Ø = Vector3(0, 0, 0)
        e = Vector3(0, 0, 5)

        X = a.x - c.x
        Y = a.y - c.y
        Z = a.z - c.z
        C = Vector3(cos(Ø.x), cos(Ø.y), cos(Ø.z))
        S = Vector3(sin(Ø.x), sin(Ø.y), sin(Ø.z))

        d = Vector3(
                C.y*(S.z*Y + c.z*X) - S.y*Z,
                S.x*(C.y*Z + S.y*(S.z*Y + c.z*X)) + C.x*(C.z*Y - S.z*X),
                C.x*(C.y*Z + S.y*(S.z*Y + c.z*X)) - S.x*(C.z*Y - S.z*X),
                )

        b = Vector2(
                (e.z/d.z)*d.x + e.x,
                (e.z/d.z)*d.y + e.y
                )

        return b


@dataclass
class Vector2:
    """
    A 2d vector.
    """
    x: float
    y: float

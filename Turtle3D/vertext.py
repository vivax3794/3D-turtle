import turtle

from .vector import Vector3


def vertext(a_: Vector3, b_: Vector3) -> None:
    """
    Draw a vertext.
    """
    a = a_.to_2d()
    b = b_.to_2d()

    turtle.penup()
    turtle.setpos(a.x, a.y)
    turtle.pendown()
    turtle.setpos(b.x, b.y)

# this is some other code I wrote to translate from 3d to 2d
from Turtle3D import Vector3, vertext


points = []
for x in [-150, -50]:
    for y in [-300, -200]:
        for z in [20, 120]:
            points.append(Vector3(x, y, z))
            print(x, y, z)


drawn = []
for a in points:
    for b in points:
        # these could be made into 1 if, but it would be long
        if a is not b:
            if sum([a.x == b.x, a.y == b.y, a.z == b.z]) == 2:
                if ((a, b) not in drawn) and ((b, a) not in drawn):
                    vertext(a, b)
                    drawn.append((a, b))
                    print(a, "->", b)


input() # keep the windows from closing

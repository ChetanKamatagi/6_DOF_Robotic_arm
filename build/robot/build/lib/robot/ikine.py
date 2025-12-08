import math

rad = 3.14159265359 / 180

def fcn(x, y, z, al1, al2, al3):
    al1 *= rad
    al2 *= rad
    al3 *= rad

    a = 22 * math.cos(al1) * math.cos(al2)
    b = 22 * math.cos(al1) * math.sin(al2)
    c = 22 * math.sin(al1)

    x1 = x - a
    y1 = y - b
    z1 = z - 0 - c

    if z1 < 0:
        zs = -1
    else:
        zs = 1

    xy = math.sqrt(x1**2 + y1**2)
    if y1 < 0:
        t1 = math.acos(x1 / math.sqrt(y1**2 + x1**2))
    else:
        t1 = -math.acos(x1 / math.sqrt(y1**2 + x1**2))

    if ((xy**2 + z1**2 + 200**2 - 168**2) / 400) / math.sqrt(xy**2 + z1**2) < 1.1:
        if ((xy**2 + z1**2 + 200**2 - 168**2) / 400) / math.sqrt(xy**2 + z1**2) > 1:
            t2 = math.acos(1) + math.acos((xy / math.sqrt(xy**2 + z1**2))) * zs
        else:
            t2 = math.acos(((xy**2 + z1**2 + 200**2 - 168**2) / 400) / math.sqrt(xy**2 + z1**2)) + math.acos(
                (xy / math.sqrt(xy**2 + z1**2))) * zs
    else:
        t2 = math.acos(((xy**2 + z1**2 + 200**2 - 168**2) / 400) / math.sqrt(xy**2 + z1**2)) + math.acos(
            (xy / math.sqrt(xy**2 + z1**2))) * zs

    if ((xy - (200 * math.cos(t2))) / 168) < 1.1 and ((xy - (200 * math.cos(t2))) / 168) > 1:
        t3 = math.acos(1) - t2
    else:
        if z1 < 200 * math.sin(t2):
            t3 = -math.acos((xy - (200 * math.cos(t2))) / 168) - t2
        else:
            t3 = math.acos((xy - (200 * math.cos(t2))) / 168) - t2

    A = math.cos(t2 + t3) * math.cos(t1)
    B = math.cos(t2 + t3) * math.sin(t1)
    C = math.sin(t2 + t3)

    d = -(A * x + B * y + C * z)

    dn = A * x1 + B * y1 + C * (z1 + 0) + d

    o = -dn / (A**2 + B**2 + C**2)
    ox = x1 + o * A
    oy = y1 + o * B
    oz = z1 + o * C

    x2 = x - ox
    y2 = y - oy
    z2 = z - oz - 0

    if z1 > 200 * math.sin(t2):
        up = -1
    else:
        up = 1

    t4 = math.asin((x2 * y1 + y2 * x1) / (math.sqrt(y1**2 + x1**2) * math.sqrt(y2**2 + x2**2 + z2**2))) * up

    if dn < 0:
        dn = -dn

    ds = dn / math.sqrt(A**2 + B**2 + C**2)

    t5 = math.acos((ds / 22))

    t6 = al3

    if t2 + t3 > 0:
        f = -1
    else:
        f = 1
    f = 1

    if t2 + t3 > al1:
        f1 = -1
    else:
        f1 = 1

    q1 = t1
    q2 = t2
    q3 = t3
    q4 = t4
    q5 = t5 * f * f1
    q6 = t6

    q1 = -q1
    q1 = q1 - 90 * rad
    q2 = -q2
    q2 = q2 + 90 * rad
    q3 = q3 - 0 * rad
    q4 = -q4
    q4 = q4 - 0 * rad
    q5 = q5
    q5 = q5 + 0 * rad
    q6 = q6 - 0 * rad

    return q1, q2, q3, q4, q5, q6

# Example usage:
x, y, z, al1, al2, al3 = 0, 0, 513, 90, 0, 0
q1, q2, q3, q4, q5, q6 = fcn(x, y, z, al1, al2, al3)
print(q1, q2, q3, q4, q5, q6)


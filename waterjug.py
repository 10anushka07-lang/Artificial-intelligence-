
def water_jug():
    jug1 = 0
    jug2 = 0
    while jug1 != 2:
        print(jug1, jug2)
        if jug1 == 0:
            jug1 = 4
        elif jug2 == 3:
            jug2 = 0
        else:
            water = min(jug1, 3 - jug2)
            jug1 -= water
            jug2 += water
    print("Goal reached!")
    print("Jug 1:", jug1, "Jug 2:", jug2)
water_jug()

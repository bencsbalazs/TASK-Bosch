def will_hit(traj: str, coords: tuple) -> bool:
    """Calculate whether the meteor hits the character or not."""

    return coords[0] == eval(traj.split("=")[1].replace("x", "*"+str(coords[1])))


print(will_hit("y = 2x - 5", (0, 0)))

def vc(roomA, roomB, position):
    if roomA == "dirty":
        print("roomA is dirty")
        print("cleaning roomA")
        roomA = "clean"
        print("roomA is clean")
        position = "roomB"
        print("moved to roomB")

    if roomB == "dirty":
        print("roomB is dirty")
        print("cleaning roomB")
        roomB = "clean"
        print("roomB is clean")
        position = "roomA"
        print("moved to roomA")

    return roomA, roomB, position


vc("dirty", "dirty", "roomA")

import math

class Point():
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def __str__(self):
        print("Point with lat, long ({}, {})".format(self.x, self.y))

    def eucDist(self, other):
        distX = math.pow(self.x - other.x, 2)
        distY = math.pow(self.y - other.y, 2)
        eucDist = math.sqrt(distX + distY)
        return eucDist

if __name__ == "__main__":
    # NOTE: Executes ONLY if ran as a script
    pointOne = Point(100, 10)
    pointTwo = Point(100, 80)
    print("testing...")
    eucDistance = Point.distance(cityOne, cityTwo)
    print("{}, and {} are a Euclidean distance of (rounded) {} apart.".format(pointOne, pointTwo, eucDistance))

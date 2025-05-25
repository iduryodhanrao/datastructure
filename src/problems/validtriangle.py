"""
All distance and triangle related problems are based on the formulas.

eg. Distance between 2 points
Input : x1, y1 = (3, 4)
           x2, y2 = (7, 7)
Output : 5
Pythogoras formula , Distance = √((x2 - x1)^2 + (y2-y1)^2)
math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

Triangle is valid:
A triangle is valid if sum of its 2 sides are greater than third.
i.e. a+b > c; a+c > b; b+c > a
if (a+b <=c) or (a+c <= b) or (b+c <=a) then false

Overlapping Rectangles
rectangle1 - l1(x,y), r1(x,y)
rectangle2 - l2(x,y), r2(x,y)
l = left top, r = right bottom
if (r1(y) < l2(y) or r2(y) < l1(y)) & (l1(x) < r2(x) or l2(x) < r1(x)) then overlap
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def do_overlap(l1, r1, l2, r2):
    # If one rectangle is to the left of the other
    if l1.x > r2.x or l2.x > r1.x:
        return False

    # If one rectangle is above the other
    if r1.y > l2.y or r2.y > l1.y:
        return False

    return True

# Driver code
if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(11, 5)
    r2 = Point(15, 0)

    if do_overlap(l1, r1, l2, r2):
        print("Rectangles Overlap")
    else:
        print("Rectangles Don't Overlap")
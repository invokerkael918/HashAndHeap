
#Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

import heapq


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        self.heap = []
        for point in points:
            distance = self.get_distance(point, origin)
            heapq.heappush(self.heap, (distance, point.x, point.y))

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(self.heap)
            result.append(Point(x, y))

        return result

    def get_distance(self, pointA, pointB):
        return (pointA.x - pointB.x) ** 2 + (pointA.y - pointB.y) ** 2
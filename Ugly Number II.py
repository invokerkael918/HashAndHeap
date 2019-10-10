import heapq
class HeapSolution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        visited = set([1])

        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2,3,5]:
                if val * factor not in visited:
                    visited.add(val* factor)
                    heapq.heappush(heap,val*factor)
        return val


class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        l = [1]
        p1, p2, p3 = 0, 0, 0

        while len(l) < n:
            v2 = l[p1] * 2
            v3 = l[p2] * 3
            v5 = l[p3] * 5
            minV = min(v2, v3, v5)
            if v2 == minV:
                p1 += 1
            if v3 == minV:
                p2 += 1
            if v5 == minV:
                p3 += 1
            l.append(minV)
        return l[-1]
import heapq


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def topk(self, nums, k):
        # write your code here
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, -num)

        result = []
        for _ in range(k):
            x = heapq.heappop(self.heap)
            result.append(-x)
   
        return result

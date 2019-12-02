import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        # write your code here
        n = len(nums)
        result = []
        maxHeap = []  # up
        minHeap = []  # down

        for i in range(n):
            if (len(maxHeap) == 0 or nums[i] <= -maxHeap[0]):
                heapq.heappush(maxHeap, -nums[i])
            else:
                heapq.heappush(minHeap, nums[i])

            self.balance(maxHeap, minHeap)

            result.append(-maxHeap[0])
        return result

    def balance(self, maxHeap, minHeap):

        while (len(maxHeap) < len(minHeap)):
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))

        while (len(minHeap) < len(maxHeap) - 1):
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

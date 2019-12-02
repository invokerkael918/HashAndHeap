import heapq

DIRECTIONS = [
    [0, 1], [0, -1], [1, 0], [-1, 0]
]


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """

    def trapRainWater(self, heights):
        # write your code here
        n, m = len(heights), len(heights[0])
        result = 0
        visited = {}
        heap = []

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    heapq.heappush(heap, (heights[i][j], i, j))
                    visited[(i, j)] = 1
                else:
                    visited[(i, j)] = 0
        while heap:
            min_height, x, y = heapq.heappop(heap)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if not self.is_valid(nx, ny, n, m):
                    continue
                if visited[(nx, ny)]:
                    continue

                nh = max(heights[nx][ny], min_height)
                result += nh - heights[nx][ny]

                heapq.heappush(heap, (nh, nx, ny))
                visited[(nx, ny)] = 1
        return result

    def is_valid(self, x, y, n, m):
        return 0 <= x < n and 0 <= y < m


if __name__ == '__main__':
    S = Solution().trapRainWater(
        [[12, 13, 0, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]])
    print(S)

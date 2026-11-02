class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        for x in range(k):
            value = heapq.heappop(max_heap)

        return -value




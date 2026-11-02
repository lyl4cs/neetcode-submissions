class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        for x in range(k):
            value = heapq.heappop(max_heap) # each pop removes the largest k
        # number so if we pop k elements from the largest then the last pop
        # is what we want
        return -value




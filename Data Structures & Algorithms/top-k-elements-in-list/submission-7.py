class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need hashmap to count the repititveness of number
        # need result list to return
        # need to for loop throuhg nums and get a count for each num
        # use K to pull the K highest counts and append them to result
        # how do i do this? ^ maybe i can sort my hashmap? and then pull k highest values and append?
        hm = {}
        result = []
        for x in nums:
            hm[x] = hm.get(x, 0) + 1
        order = sorted(hm, key = hm.get , reverse = True)

        return order[:k]



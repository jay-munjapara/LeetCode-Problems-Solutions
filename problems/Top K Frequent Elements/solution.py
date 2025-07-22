from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, index in freq.items():
            bucket[index].append(num)

        ans = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
            if len(ans) == k:
                return ans

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            diff = numbers[left] + numbers[right] - target
            if diff == 0:
                return [left + 1, right + 1]
            elif diff > 0:
                right -= 1
            else:
                left += 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            # if diff is a key in seen
            if diff in seen:
                # return the [index of the diff, current index]
                return [seen[diff], i]
            # add to dict
            seen[num] = i
        return []
        
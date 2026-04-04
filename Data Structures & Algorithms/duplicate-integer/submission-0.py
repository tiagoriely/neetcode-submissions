class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for i in nums:
            if i not in count_map:
                count_map[i] = 1
            elif i in count_map:
                return True 
        return False


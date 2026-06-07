class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permutationRecursive(0, nums)
    
    def permutationRecursive(self, i, nums):
        if i == len(nums):
            return [[]]
        
        resPerm = []
        perms = self.permutationRecursive(i + 1, nums)
        for p in perms:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                resPerm.append(pCopy)

        return resPerm
        
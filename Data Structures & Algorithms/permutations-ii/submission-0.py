class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def permutationRecursive(i):
            if i == len(nums):
                return [[]]
            
            resPerms = []
            perms = permutationRecursive(i + 1)

            # while i <= len(nums) and nums[i] == nums[i - 1]:
            #     i += 1

            for p in perms:
                for j in range(len(p) + 1):
                    copyP = p.copy()
                    copyP.insert(j, nums[i])
                    if copyP not in resPerms:
                        resPerms.append(copyP)
            return resPerms
            
        return permutationRecursive(0)
            
            

        
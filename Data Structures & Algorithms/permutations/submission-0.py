class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''recursive solution'''
        def permutation_recursive(i):
            if i == len(nums):
                return [[]]
            
            resPerms = [] # re-initialise the list
            perms = permutation_recursive(i + 1)
            for p in perms:
                for j in range(len(p) + 1): # here p is a list
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i]) # inserting at every position nums[i]
                    resPerms.append(pCopy) # add the new permutation to this level's result
            return resPerms
        
        return permutation_recursive(0)


        
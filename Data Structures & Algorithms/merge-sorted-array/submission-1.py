class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       
        L = nums1[0: m]
        
        i = 0 # index L
        j = 0 # index R
        k = 0  # index nums1

        while i < len(L) and j < len(nums2):
            
            
           
            if L[i] <= nums2[j]:
                nums1[k] = L[i]
                k += 1
                i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1

        
        while k < len(nums1) and i < len(L):
            nums1[k] = L[i]
            k += 1
            i += 1
        while j < len(nums2):
            nums1[k] = nums2[j]
            k += 1
            j += 1


        
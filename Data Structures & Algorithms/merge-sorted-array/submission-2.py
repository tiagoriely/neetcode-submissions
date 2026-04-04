class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       
       # Solution: Three Pointers Without Extra Space 1
       # Key insights:
       # • nums1 and nums2 are sorted
       # • nums1 has empty space at the end 
       # • filling from the back instead of front means never 
       #   overwrite elements we still need

        last = m + n - 1
        
        while m > 0 and n > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1

        # filling in leftovers
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1


        


        
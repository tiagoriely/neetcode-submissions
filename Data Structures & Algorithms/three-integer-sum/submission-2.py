class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        # Adding space complexity (better to use nums.sort())
        numsSorted = sorted(nums)
        print(numsSorted)

        for i in range(len(numsSorted)):

            if numsSorted[i] > 0:
                break
            
            if i > 0 and numsSorted[i] == numsSorted[i - 1]:
                continue
            
            left, right = i + 1, len(numsSorted) - 1
            target = - numsSorted[i]


            while left < right:
                currentSum = numsSorted[left] + numsSorted[right] 
                if currentSum > target:
                    right -= 1
                elif currentSum < target:
                    left += 1
                else: 
                    ans.append([-target, numsSorted[left], numsSorted[right]])
                    # With similar target you could have other combinations
                    left += 1
                    right -= 1

                    # edge case
                    while numsSorted[left] == numsSorted[left - 1] and left < right:
                        left += 1

        return ans

        
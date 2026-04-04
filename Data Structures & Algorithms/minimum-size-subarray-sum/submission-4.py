class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0, 0
        length = float("inf")

        for right in range(len(nums)):
            # increment total(i.e window), potentially reaching a total bigger or equal to target
            total += nums[right]
            while total >= target:
                # Update length of the window if shorter
                length = min(right - left + 1, length) # window size: right - left + 1
                # Reduce the total by eliminating the element at left pointer
                total -= nums[left]
                # Move the pointer reducing the size of the window
                left += 1
        return 0 if length == float("inf") else length
        
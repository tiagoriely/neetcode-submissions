# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quickSort(pairs, 0, len(pairs) - 1)
        return pairs
    
    def _quickSort(self, pairs, start, end):
        # Base case
        if end - start + 1 <= 1:
            return pairs
        
        pivot = pairs[end]
        left = start

        # Start Partition - move elements smaller than pivot on left side
        for i in range(start, end):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i] 
                pairs[i] = tmp
                left += 1
        
        # End Partition - Move pivot in-between left & right sides
        pairs[end] = pairs[left]
        pairs[left] = pivot

        # Recursive base
        self._quickSort(pairs, start, left - 1) # Quick sort left side
        self._quickSort(pairs, left + 1, end)   # Quick sort right side

        return pairs
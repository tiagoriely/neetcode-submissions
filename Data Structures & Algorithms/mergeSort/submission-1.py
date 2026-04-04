# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._sort(pairs, 0, len(pairs) - 1)

    # Helper function to implement merge sort
    def _sort(self, pairs, start, end):
        # base case
        if end - start + 1 <= 1:
            return pairs
        
        # The middle index of the array
        middle = (start + end) // 2

        # sort left half
        self._sort(pairs, start, middle)

        # sort right half
        self._sort(pairs, middle + 1, end)

        # merge sorted halfs
        self.merge(pairs, start, end, middle)

        return pairs


    def merge(self, pairs, start, end, middle):
        # Copy the sorted left & right halfs to temp arrays
        L = pairs[start: middle + 1]
        R = pairs[middle + 1: end + 1]

        i = 0 # index for L
        j = 0 # index for R
        k = start # index for array 'pairs'

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                k += 1
                i += 1
            else:
                pairs[k] = R[j]
                k += 1
                j += 1
        
        # One of the halfs will have elements remaining, add them
        # if left half has remaining elements
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        # if right half has remaining elements
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1

        return pairs




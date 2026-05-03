class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''Brute Force'''
        if x == 0 or n == 0:
            return 1
        
        count = 1
        total = 1
        while count <= abs(n):
            total *= x
            count += 1

        return total if n > 0 else 1 / total
        
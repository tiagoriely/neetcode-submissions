class Solution:
    def myPow(self, x: float, n: int) -> float:
        count = 1
        total = 1
        while count <= abs(n):
            total *= x
            count += 1

        if n > 0:
            return total
        elif n == 0:
            return 1.0
        else:
            return 1 / total
        
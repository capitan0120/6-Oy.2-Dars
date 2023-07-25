class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = bin(x^y)
        return s.count("1")
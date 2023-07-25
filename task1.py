class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        k = -1
        for i in range(len(g)):
            for j in range(k+1, len(s)):
                if g[i] <= s[j]:
                    count += 1
                    k = j
                    break
        return count
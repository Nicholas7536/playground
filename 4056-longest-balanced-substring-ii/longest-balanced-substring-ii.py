class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        max_len = 1 

        # 1-character sequences
        count = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 1

        # 2-letter combinations
        pairs = [('a','b'), ('a','c'), ('b','c')]
        for x, y in pairs:
            diff_map = {0: -1}
            diff = 0
            for i, ch in enumerate(s):
                if ch == x:
                    diff += 1
                elif ch == y:
                    diff -= 1
                else:
                    diff = 0
                    diff_map = {0: i}
                    continue
                if diff in diff_map:
                    max_len = max(max_len, i - diff_map[diff])
                else:
                    diff_map[diff] = i

        # 3-letter case
        countA = countB = countC = 0
        prefix_map = {(0,0): -1}
        for i, ch in enumerate(s):
            if ch == 'a':
                countA += 1
            elif ch == 'b':
                countB += 1
            else:
                countC += 1
            d1 = countA - countB
            d2 = countA - countC
            if (d1,d2) in prefix_map:
                max_len = max(max_len, i - prefix_map[(d1,d2)])
            else:
                prefix_map[(d1,d2)] = i

        return max_len
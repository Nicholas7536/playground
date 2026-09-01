class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def sol(i, r, d):
            if i == n and d == 4:
                res.append(r[:-1])
                return

            if i >= n or d == 4:
                return

            if s[i] == "0":
                sol(i + 1, r + "0.", d + 1)
                return

            for j in range(1, 4):
                p = s[i:i + j]

                if int(p) > 255:
                    break

                sol(i + j, r + p + ".", d + 1)

        sol(0, "", 0)
        return res     
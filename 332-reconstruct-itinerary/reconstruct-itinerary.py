from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        flights = defaultdict(list)
        for s, e in tickets:
            flights[s].append(e)
        res = []
        def dfs(root):
            while flights[root]:
                dfs(flights[root].pop())
            res.append(root)
                
        dfs("JFK")

        return res[::-1]
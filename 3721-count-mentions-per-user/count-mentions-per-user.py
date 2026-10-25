class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))
        mentions = [0] * numberOfUsers
        online, offline = set(range(numberOfUsers)), set()
        for msg, ts, m in events:
            ts = int(ts)
            online |= set(u[1] for u in offline if u[0] <= ts)
            offline = set(u for u in offline if u[0] > ts)
            if msg == "MESSAGE":
                if m == "ALL":
                    mentions = [m + 1 for m in mentions]
                elif m == "HERE":
                    mentions = [m + 1 if idx in online else m for idx, m in enumerate(mentions)]
                else:
                    for i in m.split(" "):
                        mentions[int(i[2:])] += 1
            elif msg == "OFFLINE":
                m = int(m)
                online.remove(m)
                offline.add((ts + 60, m))
        return mentions
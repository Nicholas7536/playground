class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
   
        count = 0
        maxCount = -1
        for j in range(len(seats)):
            if seats[j] == 0:
                count += 1
            else:
                if count == j:
                    count = 2*count
                maxCount = max(maxCount, count)
                count = 0
        else:
            if seats[-1] == 0:
                count = 2*count
            maxCount = max(maxCount, count)
        
        return (maxCount+1) // 2
        

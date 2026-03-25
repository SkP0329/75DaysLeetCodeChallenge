class Solution:
    def maxProfit(self,prices):
        min=prices[0]
        mp=0
        for p in prices:
            if p<min:min=p
            else:mp=max(mp,p-min)
        return mp
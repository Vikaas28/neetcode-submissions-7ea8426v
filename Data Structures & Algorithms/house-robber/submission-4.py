class Solution:
    
    def rob(self, nums: List[int]) -> int:
        #classic knapsack problem may be solve by recurison and dp also dp is an problem solving methond or technique to solve oevrlaping sub problems 
        n=len(nums)
        if n==0:
            return 0
        dp=[0]*(n+2) # extra space for storing 

        for i in range(n-1,-1,-1):
            steal=nums[i]+dp[i+2]
            skip =dp[i+1]
            dp[i]=max(steal,skip)
        return dp[i]




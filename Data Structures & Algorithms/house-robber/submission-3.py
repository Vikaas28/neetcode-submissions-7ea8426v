class Solution:
    
    def rob(self, nums: List[int]) -> int:
        #classic knapsack problem may be solve by recurison and dp also dp is an problem solving methond or technique to solve oevrlaping sub problems 
        n=len(nums)
        dp=[-1]* n
        def solve(i):
            if i>=n:
                return 0
            if dp[i] !=-1:
                return dp[i]
            steal=nums[i] + solve(i+2)
            skip = solve(i+1)
            dp[i]=max(steal,skip)
            return dp[i]
        return solve(0)           

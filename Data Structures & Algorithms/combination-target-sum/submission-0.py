class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def back(i,p,t):
            

            if t==target:
                res.append(p.copy())
                return 
            if t> target :
                return     
            for j in range(i,len(nums)) :
                p.append(nums[j])
                back(j,p,t+nums[j])
                p.pop()
        back(0,[],0)
        return res           

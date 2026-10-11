class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n=len(nums)
        result=0
        for i in range(0,n):
            dist_even=set()
            dist_odd=set()
            for j in range(i,n):
                dist_even.add(nums[j]) if nums[j]%2==0 else dist_odd.add(nums[j])
                if len(dist_even)==len(dist_odd) and result<(j-i+1):
                    result=j-i+1
        return result
                




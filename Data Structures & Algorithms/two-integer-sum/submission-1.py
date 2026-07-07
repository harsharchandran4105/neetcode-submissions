class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out=[]
        for i in range(len(nums)):
            a=target-nums[i]
            if a in nums and nums.index(a) != i:
                out.append(i)
                out.append(nums.index(a))
                break
            
        return sorted(out)
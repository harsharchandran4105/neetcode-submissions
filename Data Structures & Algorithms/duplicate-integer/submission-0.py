class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        s=set(nums)
        l2=len(s)
        if l==l2:
            return False
        else:
            return True
        
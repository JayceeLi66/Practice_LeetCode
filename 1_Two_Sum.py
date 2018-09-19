class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for x in range(l) :
            for y in range(x+1, l):
                if target == nums[x]+nums[y] :
                    return [x,y]
        return "No solution exists"

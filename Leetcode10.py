class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            index = len(nums)//2
            if target == nums[index]:
                return index
            elif target < nums[index]:
                return self.searchInsert(nums[:index], target)
            else:
                return index + 1 + self.searchInsert(nums[index + 1:], target)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pointer: int = 0
        zero_pointer: int = len(nums)
        while non_zero_pointer < zero_pointer:
            if nums[non_zero_pointer] == 0:
                nums.append(0)
                del nums[non_zero_pointer]
                zero_pointer -= 1
            else:
                non_zero_pointer += 1
        return  nums

class Solution:
    def twoSum(self, nums: list, target: int):
        
        o = nums[0]
        
        while o < len(nums):
        
            i = 0

            for i in nums:

                if nums[i] == nums[o]:
                    continue

                elif nums[i] + nums[o] == target:
                    return nums[i], nums[o]
                    break

                else: continue
            
            o += 1

test_1 = Solution()

test_1.twoSum([3, 6, 5, 4, 8], 7)



from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_array = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if sorted_array[left] + sorted_array[right] > target:
                right -= 1
            elif sorted_array[left] + sorted_array[right] < target:
                left += 1
            else:
                break

        first = sorted_array[left]
        second = sorted_array[right]

        if nums.index(first) == nums.index(second):
            return [nums.index(first), nums.index(second, nums.index(first) + 1)]

        return [nums.index(first), nums.index(second)]


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            if values.get(target - num) is not None:
                return [i, values[target - num]]
            values[num] = i
        return []


if __name__ == '__main__':
    so = Solution3()
    print(so.twoSum([2, 7, 11, 15], 9))
    print(so.twoSum([3, 2, 3], 6))
    print(so.twoSum([3, 2, 4], 6))
    # print(so.twoSum([3, 3], 6))
    print(so.twoSum([5, 75, 25], 100))
    # print(so.twoSum([0, 3, -3, 4, -1], -1))

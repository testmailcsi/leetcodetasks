from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(f"{nums[i]} + {nums[j]}")
                if nums[i] + nums[j] == target:
                    print(f"Найдено {nums[i]} + {nums[j]} = {target}")
                    return [i, j]  # Возвращаем результат
        return []

solution = Solution()

nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print(f"Результат для {nums} с target={target}: {result}\n")

nums1 = [2, 7, 11, 15]
target1 = 9  # Исправлено с 6 на 9, так как 2+7=9
result1 = solution.twoSum(nums1, target1)
print(f"Результат для {nums1} с target={target1}: {result1}\n")

nums2 = [3, 3]
target2 = 6
result2 = solution.twoSum(nums2, target2)
print(f"Результат для {nums2} с target={target2}: {result2}")
class Solution:
    def threeSum(self, nums, total):
        results = []
        # O(nlogn) operation
        nums.sort()
        length_nums = len(nums)
        for i in range(0, length_nums - 1): # 0 -> n - 2
            a = nums[i]
            start = i + 1
            end = length_nums - 1

            while start < end:
                b = nums[start]
                c = nums[end]
                total_sum = a + b + c
                if total_sum == total:
                    results.append((a, b, c))

                    if nums[b+1] == b:
                        start = start + 1
                    else:
                        end = end - 1
                elif total_sum > total:
                    end -= 1
                else:
                    start += 1

        return results

solution = Solution()

print solution.threeSum([-1,7,-4 , 2, 2, 9], 8)



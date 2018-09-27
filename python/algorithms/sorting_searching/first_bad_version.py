# class Solution:
#     def firstBadVersion(self, n):
#         return self.helper(1, n)
#
#     def helper(self, lower, upper):
#         if lower == upper:
#             return lower
#
#         mid = (lower + upper)/2
#
#         if isBadVersion(mid) and mid > 1 and not isBadVersion(mid - 1):
#             return mid
#         elif isBadVersion(mid):
#             if mid == 1:
#                 return mid
#             else:
#                 return self.helper(lower, mid - 1)
#         else:
#             return self.helper(mid+1, upper)
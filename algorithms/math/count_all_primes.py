class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0

        prime_list=[True] * n
        prime_list[0] = False
        prime_list[1] = False

        for i in range(2, int(n**0.5)+1):
            if prime_list[i] == True:
                start_val = i
                while start_val < n:
                    start_val = start_val + i
                    if start_val <= len(prime_list) - 1:
                        prime_list[start_val] = False
        counter = 0

        for i in range(0, len(prime_list)):
            if prime_list[i] == True:
                counter += 1

        return counter

solution = Solution()
print(solution.countPrimes(200))

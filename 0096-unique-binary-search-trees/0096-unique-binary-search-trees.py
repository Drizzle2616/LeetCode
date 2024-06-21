class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize the DP array with 0's and set dp[0] to 1
        dp = [0] * (n + 1)
        dp[0] = 1

        # Compute the number of unique BSTs for each number of nodes up to n
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[n]

# Example usage
solution = Solution()
print(solution.numTrees(3))  # Output: 5
print(solution.numTrees(1))  # Output: 1

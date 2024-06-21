class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows <= 0:
            return []
        
        # Initialize the result with the first row
        triangle = [[1]]
        
        # Generate each row of the Pascal's triangle
        for i in range(1, numRows):
            prev_row = triangle[i - 1]
            new_row = [1]  # Start with the first 1
            
            # Generate the intermediate values of the row
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            
            new_row.append(1)  # End with the last 1
            triangle.append(new_row)
        
        return triangle

# Example usage:
solution = Solution()
print(solution.generate(5))  # Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
print(solution.generate(1))  # Output: [[1]]

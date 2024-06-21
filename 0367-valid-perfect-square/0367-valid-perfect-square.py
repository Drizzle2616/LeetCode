class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if using sqrt func
        # rounded_sqrt = round(sqrt(num))
        # return rounded_sqrt == num 

        # without using sqrt func 
        low = 1
        high = num
        
        while high >= low:
            middle = (high + low) // 2
            middle_sqrd = middle * middle
            if middle_sqrd == num:
                return True
            elif middle_sqrd < num:
                low = middle + 1
            # This could be else, but I thought this would be easier to understand.
            elif middle_sqrd > num:
                high = middle - 1
        
        return False
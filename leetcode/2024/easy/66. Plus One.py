class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        remainder = 1
        ind = len(digits) - 1

        while remainder == 1:
            if ind == -1:
                digits = [1] + digits
                remainder = 0

            result = digits[ind] + remainder
            if result == 10:
                remainder = 1
                result = 0
            else:
                remainder = 0

            digits[ind] = result
            ind -= 1

        return digits


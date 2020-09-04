class Solution(object):
    def plusOne(self, digits):  # 加一  大数加减
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = False
        first_plus = False
        for i in range(len(digits) - 1, -1, -1):
            if ((i + 1) == len(digits)) & (digits[i] == 9):
                digits[i] = 0
                flag = True
                if i == 0:
                    first_plus = True
                continue
            else:
                if i + 1 == len(digits):
                    digits[i] = digits[i] + 1

            if flag & (digits[i] == 9):
                if i == 0:
                    first_plus = True
                digits[i] = 0
                flag = True
            else:
                if flag:
                    digits[i] = digits[i] + 1
                    flag = False

        if first_plus:
            return [1] + digits

        return digits


if __name__ == '__main__':
    print(Solution.plusOne(Solution.__class__, [9]))

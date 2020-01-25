class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """

    def intToRoman(self, n):
        # write your code here
        digitList = []
        s = ""
        while (n != 0):
            digitList.append(n % 10)
            n = n // 10
        # print(digitList)
        s = self.helper(digitList)

        return s

    def helper(self, digitList):
        digitMap = {
            3: ["M", "MM", "MMM"],
            2: ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            1: ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            0: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        }
        s = ""
        for index, digit in enumerate(digitList):
            if digit == 0:
                continue
            s = digitMap[index][digit - 1] + s
        return s


if __name__ == '__main__':
    S = Solution().intToRoman(123)
    print(S)

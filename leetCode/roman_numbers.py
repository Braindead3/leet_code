class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_of_roman = 0
        i = 0
        roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        while i < len(s):
            try:
                asd = s[i] + s[i + 1]
            except IndexError:
                asd = 'net'
            if asd in roman_num:
                sum_of_roman += roman_num.get(asd, None)
                i += 1
            else:
                sum_of_roman += roman_num.get(s[i], None)
            i += 1
        return sum_of_roman


if __name__ == '__main__':
    so = Solution()
    print(so.romanToInt('III'))

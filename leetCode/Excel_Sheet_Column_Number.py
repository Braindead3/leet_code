class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                   'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                   'X': 24, 'Y': 25, 'Z': 26}
        corresponding_column_number = 0
        if len(columnTitle) == 1:
            return letters.get(columnTitle[0])
        else:
            for i in range(len(columnTitle)):
                corresponding_column_number += letters.get(columnTitle[i]) * 26 ** (len(columnTitle) - i - 1)
        return corresponding_column_number

    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while num > 0:
            result.append(capitals[(num - 1) % 26])
            num = (num - 1) // 26
        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    so = Solution()
    print(so.titleToNumber('ZY'))
    print(so.convertToTitle(701))

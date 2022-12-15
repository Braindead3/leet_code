class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) == 1:
            return strs[0]

        min_length = len(strs[0])
        for word in strs:
            cur_len = len(word)
            if min_length > cur_len:
                min_length = cur_len

        for i in range(0, min_length):
            current = strs[0][i]
            for word in strs:
                if word[i] != current:
                    return result
            result += current
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.longestCommonPrefix(["flower", "flower", "flower", "flower"]))
    print(so.longestCommonPrefix(["flower", "flow", "flight"]))
    print(so.longestCommonPrefix(["a", "a", "b"]))

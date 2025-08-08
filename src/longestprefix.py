class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            current_string = strs[i]
            j = 0

            while j < len(prefix) and j < len(current_string) and prefix[j] == current_string[j]:
                j += 1

            prefix = prefix[:j]
            if not prefix:
                return ""
        return prefix

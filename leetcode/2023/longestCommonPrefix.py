class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # f fl flo flow
        # w ow low -- flow
        # l lo -- low
        # -- fl lo flo
        # o -- lo
        # n + (n-1) + (n-2) -> n2

        common_prefix = ""

        first_word = strs[0]
        second_word = strs[1]

        for i in range(len(first_word)):
            prefix = first_word[0 : i + 1]
            if second_word.startswith(prefix) and len(common_prefix) < len(prefix):
                common_prefix = prefix

        for word in strs:
            while common_prefix and not word.startswith(common_prefix):
                common_prefix = common_prefix[0 : len(common_prefix) - 1]

        return common_prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                res += a[0]
            else:
                return res
        return res


print(list(zip(*["flower", "flow", "flight"])))

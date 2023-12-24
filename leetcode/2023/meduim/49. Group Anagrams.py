class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_dict(s):
            temp_dict = {}

            for char in s:
                value = temp_dict.get(char, 0) + 1
                temp_dict[char] = value

            return temp_dict

        targets = [[strs[0]]]
        for index in range(1, len(strs)):
            for t in targets:
                t_dict = create_dict(t[0])
                s_dict = create_dict(strs[index])
                if t_dict == s_dict:
                    t.append(strs[index])
                    break
            else:
                targets.append([strs[index]])

        return targets


class SolutionOPTIMAL:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = {}

        for s in strs:
            vector = {i: 0 for i in "abcdefghnt"}
            for char in s:
                vector[char] += 1

            key = "".join(str(vector.items()))

            b = buckets.get(key, [])
            b.append(s)
            buckets[key] = b

        return buckets.values()

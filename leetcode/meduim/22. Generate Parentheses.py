from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        target_list = []
        self.backtrack(target_list, "", n)
        return target_list


    def backtrack(self, target_list: list, current_str:str, max_n:int):
        if len(current_str) == max_n*2:
            target_list.append(current_str)
            print(current_str)
            return

        if current_str.count("(") < max_n:
            self.backtrack(target_list, current_str+ "(", max_n)

        if current_str.count("(") > current_str.count(")"):
            self.backtrack(target_list, current_str+ ")", max_n)




s = Solution()

print(s.generateParenthesis(3))
print(s.generateParenthesis(2))
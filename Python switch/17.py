class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums_map = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
        }
        res = []
        def backtrack(index, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            for ch in nums_map[digits[index]]:
                backtrack(index + 1, curr_str + ch)
        if digits:
            backtrack(0, "")
        return res
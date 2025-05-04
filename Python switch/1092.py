class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        dp = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
        for i in range(len(str1) - 1, -1, -1):
            for j in range(len(str2) - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        res = ""
        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                res += str1[i]
                i+=1
                j+=1
            else:
                if dp[i][j+1] > dp[i+1][j]:
                    res += str2[j]
                    j+=1
                else:
                    res += str1[i]
                    i+=1
        return res+str1[i:]+str2[j:]
def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    lcs = ""
    dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
                lcs = text1[i] + lcs
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    return dp[0][0], lcs

res, lcs = longestCommonSubsequence(text1 = "abcde", text2 = "ace")

print (res, lcs) # 3 ace
def makeFancyString(s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        count = 0
        prev = ""
        for ch in s:
            if prev == ch:
                count += 1
                if count >= 2:
                    continue
                else:
                    prev = ch
                    res += ch
            else:
                prev = ch
                count = 0
                res += ch
        return res
print(makeFancyString("leeetcode"))
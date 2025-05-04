def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(s) < len(t):
        return ""
    
    need_map, have_map = {}, {}

    for ch in t:
        need_map[ch] = 1 + need_map.get(ch, 0)

    need, have = len(need_map), 0
    lptr = 0
    min_substr, min_length = [], float("infinity")

    # i basically acts as a right pointer in the window
    for i in range(len(s)):
        current_char = s[i]
        have_map[current_char] = 1 + have_map.get(current_char, 0)

        if current_char in need_map and have_map[current_char] == need_map[current_char]:
            have += 1

        while have == need:
            if (i - lptr + 1) < min_length:
                print(min_substr)
                min_substr = [lptr, i]
                min_length = i - lptr + 1
            
            # Pop elements from left => Means decrement by one in have_map
            have_map[s[lptr]] -= 1
            if s[lptr] in need_map and have_map[s[lptr]] < need_map[s[lptr]]:
                have -= 1
            # print(lptr)
            lptr += 1
    
    if len(min_substr) == 0:
        return ""
    return s[min_substr[0]: min_substr[1]+1]


    
print(minWindow(s = "aa", t = "aa"))
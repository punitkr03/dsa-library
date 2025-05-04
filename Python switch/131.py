class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        n = len(s)

        def is_palindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def possible_partitions(idx, current_list):
            is_prev_palindrome = is_palindrome(current_list[-1])
            if idx == n:
                if is_prev_palindrome:
                    result.append(current_list[:])
                return
            if is_prev_palindrome:
                current_list.append(s[idx])
                possible_partitions(idx + 1, current_list)
                current_list.pop()
            current_list[-1] = current_list[-1] + s[idx]
            possible_partitions(idx + 1, current_list)
            current_list[-1] = current_list[-1][:-1]

        possible_partitions(1, [s[0]])
        return result
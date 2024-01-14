class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        string res = "";
        sort(strs.begin(), strs.end());
        int strs_size = strs.size();
        string first = strs[0], last = strs[strs_size - 1];
        int minSize = first.size();
        for (int i = 0; i < minSize; i++)
        {
            if (first[i] != last[i])
                return res;
            res += first[i];
        }
        return res;
    }
};
class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        unordered_map<int, int> res;
        for (auto x : nums)
            res[x]++;
        for (auto z : res)
            if (z.second == 1)
                return z.first;
        return -1;
    }
};
//Editorial answer for syntax reference
class Solution
{
public:
    bool uniqueOccurrences(vector<int> &arr)
    {
        unordered_map<int, int> umap;
        unordered_set<int> uset;
        for (auto num : arr)
        {
            umap[num]++;
        }
        for (auto i : umap)
        {
            if (!uset.insert(i.second).second)
                return false;
        }
        return true;
    }
};
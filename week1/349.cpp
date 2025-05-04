class Solution
{
public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        int hashTable[1000] = {0};
        vector<int> res;
        for (int i = 0; i < nums1.size(); i++)
        {
            if (hashTable[nums1[i]] == 0)
                hashTable[nums1[i]]++;
        }
        for (int i = 0; i < nums2.size(); i++)
        {
            if (hashTable[nums2[i]] != 0)
            {
                res.push_back(nums2[i]);
                hashTable[nums2[i]]--;
            }
        }
        return res;
    }
};
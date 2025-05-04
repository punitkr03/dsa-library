class Solution
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        int firstOcc = -1, lastOcc = -1;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == target)
            {
                firstOcc = i;
                break;
            }
        }
        for (int j = nums.size() - 1; j >= 0; j--)
        {
            if (nums[j] == target)
            {
                lastOcc = j;
                break;
            }
            if (j < firstOcc)
            {
                break;
            }
        }

        vector<int> ans;
        ans.push_back(firstOcc);
        ans.push_back(lastOcc);
        return ans;
    }
};

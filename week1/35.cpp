class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int s = 0, e = nums.size() - 1, ans;
        while (s <= e)
        {
            int mid = s + (e - s) / 2;
            if (target < nums[mid])
            {
                e = (mid - 1);
                ans = e + 1;
            }
            else if (target > nums[mid])
            {
                s = (mid + 1);
                ans = s;
            }
            else
            {
                return mid;
            }
        }
        return ans;
    }
};
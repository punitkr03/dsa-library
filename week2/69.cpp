class Solution
{
public:
    int mySqrt(int x)
    {
        long long int s = 0, e = x, ans = 0;
        if (x == 1)
            return 1;
        while (s <= e)
        {
            long long int mid = s + (e - s) / 2;
            long long int square = mid * mid;
            if (square == x)
            {
                return mid;
            }
            else if (square > x)
            {
                e = mid - 1;
            }
            else
            {
                ans = mid;
                s = mid + 1;
            }
        }
        return ans;
    }
};
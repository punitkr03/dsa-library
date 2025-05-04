class Solution
{
public:
    bool halvesAreAlike(string s)
    {
        int n = s.length();
        int slice = n / 2;
        int v1 = 0, v2 = 0;
        for (int i = 0; i < slice; i++)
        {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')
            {
                v1++;
            }
        }
        for (int i = slice; i < n; i++)
        {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')
            {
                v2++;
            }
        }
        return v1 == v2;
    }
};
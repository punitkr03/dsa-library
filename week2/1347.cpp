class Solution {
public:
    int minSteps(string s, string t) {
        unordered_map<char,int>s_count;
        unordered_map<char,int>t_count;
        int count=0;
        for(auto a:s)s_count[a]++;
        for(auto a:t)t_count[a]++;

        for (auto a : s_count) {
            if (t_count.find(a.first) != t_count.end()) {
                if (s_count[a.first] == t_count[a.first]) {
                    count += s_count[a.first];
                } else {
                    count += min(s_count[a.first], t_count[a.first]);
                }
            }
        }

        return s.size()-count;
    }
};


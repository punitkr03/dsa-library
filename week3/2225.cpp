class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        map<int, int> scoresLoserMap;
        vector<vector<int>> ans;
        set<int> winners;
        vector<int> losers;
        int totalMatches = matches.size();

        for (int i = 0; i < totalMatches; i++){
            int winner = matches[i][0];
            int loser = matches[i][1];
            scoresLoserMap[loser]++;
        }

        for (int i = 0; i < totalMatches; i++){
            int winner = matches[i][0];
            if(scoresLoserMap.find(winner) == scoresLoserMap.end()) {
                winners.insert(winner);
            }
        }

        for (const auto& pair : scoresLoserMap) {
            if (pair.second == 1) {
                losers.push_back(pair.first);
            }
        }
        vector<int> v(winners.begin(), winners.end());
        ans.push_back(v);
        ans.push_back(losers);
        return ans;
    }
};
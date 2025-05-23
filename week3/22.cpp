class Solution {
public:
    void solve(string valid, int open, int close, vector<string> &ans){
        if(open == 0 && close == 0){
            ans.push_back(valid);
            return;
        }
        if(open == close){
            string op1 = valid;
            op1.push_back('(');
            solve(op1, open-1, close, ans);
        }
        else if(open == 0){
            //only choice is to put close brackets 
            string op1 = valid;
            op1.push_back(')');
            solve(op1, open, close-1, ans);
        }
        else if(close == 0){
            //only choise is to use open bracket 
            string op1 = valid;
            op1.push_back('(');
            solve(op1, open-1, close, ans);
        }
        else{
            string op1 = valid;
            string op2 = valid;
            op1.push_back('(');
            op2.push_back(')');
            solve(op1, open-1, close, ans);
            solve(op2, open, close-1, ans);
        }
    }
    vector<string> generateParenthesis(int n) {
        int open = n;
        int close = n;
        vector<string> ans;
        string valid = "";
        solve(valid, open, close, ans);
        return ans;
    }
};
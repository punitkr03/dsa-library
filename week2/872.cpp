/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void DFS (TreeNode* root, vector<int>& ans) {
        if(!root)
        return;
        if(!root->right && !root->left)
            ans.push_back(root->val);
        DFS(root->right, ans);
        DFS(root->left, ans);
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> tree1, tree2;
        DFS(root1, tree1);
        DFS(root2, tree2);
        return tree1==tree2;
    }
};
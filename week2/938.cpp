class Solution
{
public:
    int rangeSumBST(TreeNode *root, int low, int high)
    {
        if (!root)
            return 0;
        if (root->val >= low && root->val <= high)
        {
            int curr = root->val;
        }
        else
        {
            curr = 0;
        }
        int ls = rangeSumBST(root->left, low, high);
        int rs = rangeSumBST(root->right, low, high);

        return curr + ls + rs;
    }
};
/*****************************************************
 *
 *  938. Range Sum of BST solution c++
 *
 *  Using recursion
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

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

void rec(TreeNode *root, int l, int h, int &sum)
{
    if (root == nullptr)
        return;

    rec(root->left, l, h, sum);
    if (root->val >= l && root->val <= h)
        rec(root->right, l, h, sum += root->val);
    else
        rec(root->right, l, h, sum);
}

int rangeSumBST(TreeNode *root, int low, int high)
{
    int ans = 0;
    rec(root, low, high, ans);

    return ans;
}

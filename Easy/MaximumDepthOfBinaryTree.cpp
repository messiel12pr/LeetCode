/*****************************************************
 *
 *  104. Maximum Depth of Binary Tree solution c++
 * 
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
 
int rec(TreeNode *root)
{
    if (root == nullptr)
        return 0;

    int l = rec(root->left);
    int r = rec(root->right);

    if (l > r)
        return 1 + l;

    return 1 + r;
}

int maxDepth(TreeNode *root)
{
    return rec(root);
}

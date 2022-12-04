/*****************************************************
 *
 *  700. Search in a Binary Search Tree solution c++
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
 
TreeNode *rec(TreeNode *root, int val)
{
    if (root == nullptr)
        return nullptr;

    if (root->val == val)
        return root;

    if (root->val > val)
        return rec(root->left, val);

    return rec(root->right, val);
}

TreeNode *searchBST(TreeNode *root, int val)
{
    return rec(root, val);
}

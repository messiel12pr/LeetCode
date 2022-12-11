/*****************************************************
 *
 *  100. Same Tree solution c++
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
 
bool rec(TreeNode *l, TreeNode *r)
{
    if (l == nullptr && r == nullptr)
        return true;

    if (l == nullptr || r == nullptr)
        return false;

    if (l->val != r->val)
        return false;

    return rec(l->left, r->left) && rec(l->right, r->right);
}

bool isSameTree(TreeNode *p, TreeNode *q)
{
    return rec(p, q);
}

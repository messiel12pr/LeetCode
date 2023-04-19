/*****************************************************
 *
 *  145. Binary Tree Postorder Traversal solution c++
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
 
void rec(TreeNode *root, vector<int> &ans)
{
    if (root == nullptr)
        return;

    rec(root->left, ans);
    rec(root->right, ans);
    ans.push_back(root->val);
}

vector<int> postorderTraversal(TreeNode *root)
{
    vector<int> ans;

    rec(root, ans);

    return ans;
}

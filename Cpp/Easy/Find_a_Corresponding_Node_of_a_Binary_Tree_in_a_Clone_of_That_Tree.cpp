/**
 * 
 *  1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
 * 
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    void search(TreeNode* head, TreeNode* target, TreeNode* &ans)
    {
        if(head == nullptr)
            return;

        search(head->left, target, ans);
        if(head->val == target->val)
        {
            ans = head;
            return;
        }
        search(head->right, target, ans);
    }

    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) 
    {
        TreeNode* ans;
        search(cloned, target, ans);
        return ans;
    }
};

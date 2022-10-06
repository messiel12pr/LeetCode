/*****************************************************
 *
 *  234. Palindrome Linked List solution c++
 *
 *  Using stack
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

bool isPalindrome(ListNode *head)
{
	ListNode *current = head;
	stack<int> myStack;
	int c = 0;

	while (current != nullptr)
	{
		myStack.push(current->val);
		current = current->next;
		c++;
	}

	current = head;

	for (int i = 0; i < c / 2; i++)
	{
		if (current->val != myStack.top())
			return false;

		current = current->next;
		myStack.pop();
	}

	return true;
}

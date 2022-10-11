/*****************************************************
 *
 *  2181. Merge Nodes in Between Zeros solution c++
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

ListNode *mergeNodes(ListNode *head)
{
	ListNode *prev, *current, *anchorL, *anchorR, *dummy = head;
	int sum = 0;
	anchorL = head;

	while (current != nullptr)
	{
		if (current->val != 0)
		{
			// If the node is in between the 0's sum and store the value
			sum += current->val;
		}

		else
		{
			// Update our pointers and store our sum in the list
			dummy = anchorL;
			anchorL->val = sum;
			anchorL = anchorL->next;
			sum = 0;
			anchorR = current;
		}
		// Continue traversing the list
		current = current->next;
	}

	// Delete first node (It's 0)
	prev = head;
	current = head->next;
	head = current;
	delete prev;

	// Delete the nodes after our sums
	dummy->next = nullptr;

	return head;
}

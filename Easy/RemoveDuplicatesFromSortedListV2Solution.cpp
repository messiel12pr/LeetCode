/********************************************************
 *
 *  83. Remove Duplicates from Sorted List solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*******************************************************

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

ListNode *deleteDuplicates(ListNode *head)
{
	if (head == nullptr)
		return head;

	ListNode *current = head->next;
	ListNode *prev = head;

	while (current != nullptr)
	{
		if (prev->val == current->val)
		{
			prev->next = current->next;
			delete current;
			current = prev->next;
		}

		else
		{
			prev = current;
			current = current->next;
		}
	}

	return head;
}

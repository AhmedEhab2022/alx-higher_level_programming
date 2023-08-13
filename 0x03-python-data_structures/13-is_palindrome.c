#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: adderss of pointer to first node of linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int arr[100000];
	int no_node, i, j;
	listint_t *list_ptr;

	if (*head == NULL)
		return (1);

	list_ptr = *head;
	for (i = 0; list_ptr; ++i)
	{
		arr[i] = list_ptr->n;
		list_ptr = list_ptr->next;
	}
	no_node = i;
	i = 0;
	j = no_node - 1;
	while (i < j)
	{
		if (arr[i] != arr[j])
			return (0);
		i++;
		j--;
	}
	return (1);
}

#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p1, *p2;

	if (list == NULL)
		return (0);

	p1 = list;
	p2 = list->next;
	if (p1 == p2)
		return (1);

	while (p1->next != NULL)
	{
		while (p2->next != NULL)
		{
			if (p1 == p2)
				return (1);

			p2 = p2->next;
		}
		p1 = p1->next;
		p2 = p1->next;
	}
	return (0);
}

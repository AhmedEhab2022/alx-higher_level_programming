#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer to the head of a singly linked list.
 * @number: number to be set in new node.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *last, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	current = *head;
	while (current->n <= number && current->next != NULL)
	{
		last = current;
		current = current->next;
	}
	if (current == *head)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else if (current->next == NULL && current->n <= number)
	{
		new_node->next = NULL;
		current->next = new_node;
	}
	else
	{
		last->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}

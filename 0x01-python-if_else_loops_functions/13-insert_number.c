#include "lists.h"

/**
 * insert_node - inserts a not into a sorted list
 * @head: double pointer to a linked list
 * @number: number to be inserted
 * Return: a pointer to the inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = NULL, *after = NULL;
	int flag = 0;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}

	current = *head;
	if (number <= current->n)
	{
		*head = new;
		new->next = current;
		return (*head);
	}

	if (number > current->n && !current->next)
	{
		current->next = new;
		return (new);
	}

	after = current->next;
	while (current)
	{
		if (!after)
		{
			current->next = new;
			flag = 1;
		}
		else if (after->n == number)
		{
			current->next = new;
			new->next = after;
			flag = 1;
		}
		else if (number > current->n && number < after->n)
		{
			current->next = new;
			new->next = after;
			flag = 1;
		}
		if (flag)
			break;
		current = current->next, after = after->next;
	}
	return (new);
}

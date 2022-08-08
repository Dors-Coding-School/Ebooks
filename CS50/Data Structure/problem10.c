#include <stdlib.h>
#include <stdio.h>
// Represents a node in a hash table
typedef struct node
{
 int x;
 struct node *next;
}
node;
int main(void)
{
 // Hash table
 node *table[5];
 //Create space for a node
 node *temp1 = malloc(sizeof(node));
 //Set next field of temp to NULL
 temp1->next = NULL;
 //Set pointer at 0 to node
 table[0] = temp1;
 node *temp2 = malloc(sizeof(node));
 temp2->next = temp1;
 table[0] = temp2;
}

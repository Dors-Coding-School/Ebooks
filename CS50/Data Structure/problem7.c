#include <stdio.h>
#include <stdlib.h>
typedef struct person
{
 struct person *parents[2];
 char alleles[2];
}
person;
int main(void){
 person *p1 = malloc(sizeof(person));
 p1->alleles[0] = 'A';
 p1->alleles[1] = 'O';
 p1->parents[0] = NULL;
 p1->parents[1] = NULL;
 person *p2 = malloc(sizeof(person));
 p2->alleles[0] = 'A';
 p2->alleles[1] = 'B';
 p2->parents[0] = NULL;
 p2->parents[1] = NULL;
 person *child = malloc(sizeof(person));
 child->alleles[0] = 'A';
 child->alleles[1] = 'A';
 child->parents[0] = p1;
 child->parents[1] = p2;
 printf("%c\n", child->parents[1]->alleles[1]);
}

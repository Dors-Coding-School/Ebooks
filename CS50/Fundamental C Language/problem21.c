#include <stdlib.h>
#include <stdio.h>
int test(int x, int y);
int main(void)
{
 printf("%d\n",test(123, 456));
 printf("%d\n",test(12, 512));
 printf("%d\n",test(7, 87));
 printf("%d\n",test(12, 45));
} 
int test(int x, int y)
{
 return abs(x % 10) == abs(y % 10);
}

#include <stdio.h>

int test(int x, int y);

int main(void)
{
 printf("%d\n",test(100, 199));
 printf("%d\n",test(250, 300));
 printf("%d\n",test(105, 190));
} 

int test(int x, int y)
{
 return (x >= 100 && x <= 200) || (y >= 100 && y <= 200);
}

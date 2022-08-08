#include <stdlib.h>
#include <stdio.h>
int test(int x, int y);
int main(void)
{
 printf("%d\n",test(78, 95));
 printf("%d\n",test(95, 95));
 printf("%d\n",test(99, 70));
} 
int test(int x, int y)
{
 int val = abs(x - 100);
 int val2 = abs(y - 100);
 if (val == val2)
 {
  return 0;
 }
 else
 {
   if (val < val2)
   {
      return x;
   }
   else
   {
      return y;
   }
 }
}

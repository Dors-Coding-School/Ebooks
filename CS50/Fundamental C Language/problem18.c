#include <cs50.h>
#include <stdio.h>
int main(void)
{
 int x = get_int("What's your change?\n");
 int count_of_quarters = 0;
 while (x >= 25)
 {
   x -= 25;
   count_of_quarters += 1;
 }
 printf("%d\n", count_of_quarters);
}

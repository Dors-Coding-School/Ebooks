#include <cs50.h>
#include <stdio.h>
int main(void)
{
 int rows = get_int("Input no. of rows:\n");
 for(int i=1;i<=rows;i++)
 {
   for(int j=1;j<=i;j++)
   {
      printf("*\n");
   }
 }
}

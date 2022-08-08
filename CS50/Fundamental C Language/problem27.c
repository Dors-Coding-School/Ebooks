#include <cs50.h>
#include <stdio.h>
int main(void)
{
 int k=1;
 rows = get_int("Input number of rows :\n ");
 for(int i=1;i<=rows;i++)
 {
   for(int j=1;j<=i;j++)
   {
     printf("%d ",k);
     k++;
   }
   printf("\n");
 }
}

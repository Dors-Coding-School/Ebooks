#include <cs50.h>
#include <stdio.h>
int main(void)
{
 // Prompt user for x
 int x = get_int("x: ");
 // Prompt user for y
 int y = get_int("y: ");
 // Compare x and y
 if (x == y)
 {
  printf("YES\n");
 }
 else
 {
  printf("NO\n");
 }
}

#include <cs50.h>
#include <stdio.h>

int test(int x, int y);

int main(void)
{
 int a = get_int("What is the first number?\n");
 int b = get_int("What is the second number?\n");
 int result = test(a, b);
 printf("The result is %d\n", result);
}

int test(int x, int y)
{
 if (x == y)
 {
  return 3*(x+y);
 }
 else
 {
  return x + y;
 }
}

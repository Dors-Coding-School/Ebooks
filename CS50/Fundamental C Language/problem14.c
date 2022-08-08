#include <cs50.h>
#include <stdio.h>

int test(int x, int y);

int main(void){
 int a = get_int("What is the first number?\n");
 int b = get_int("What is the second number?\n");
 int result = test(a, b);
 printf("The result is %d\n", result);
}

int test(int x, int y)
{
 return x == 30 || y == 30 || (x + y == 30);
}

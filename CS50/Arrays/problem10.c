#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
int main(void)
{
 string s = "ILOVEYOU";
 printf("After: ");
 for (int i = 0, n = strlen(s); i < n; i++)
 {
    printf("%c", s[i] + 1);
 }
}

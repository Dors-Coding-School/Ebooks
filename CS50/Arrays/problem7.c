#include <stdio.h>
#include <cs50.h>
#include <string.h>
int main(void)
{
 string s = get_string("Input: \n");
 for (int i = 0; i < strlen(s); i++)
 {
    printf("%i", s[i] - 'a');
 }
 printf("\n");
}

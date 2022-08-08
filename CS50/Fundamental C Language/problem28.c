#include <cs50.h>
#include <stdio.h>

int get_num_digits(long card_num);

int main(void)
{
 int num = get_int("What's your number? \n");
 int num_digits = get_num_digits(num);
 printf("Your number has %d digits\n", num_digits);
}

int get_num_digits(long card_num)
{
 int count = 0;
 while (card_num != 0)
 {
   card_num /= 10;
   count += 1;
 }
 return count;
}

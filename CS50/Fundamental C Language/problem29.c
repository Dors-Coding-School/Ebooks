#include <cs50.h>
#include <stdio.h>

int sum_digits(long card_num);

int main(void)
{
 int num = get_int("What's your number? \n");
 int num_digits = sum_digits(num);
 printf("Your number sum of digits is %d\n", num_digits);
}

int sum_digits(long card_num)
{
 int sum = 0;
 while (card_num > 0)
 {
   sum += (card_num % 10)
   card_num /= 10;
 }
 return sum;
}

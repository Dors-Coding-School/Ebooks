#include <stdio.h>

void cough(int x);

int main(void)
{
 printf("Cough\n");
 printf("Cough\n");
 printf("Cough\n");
 for (int i = 0; i < 3; i ++)
 {
  printf("Cough\n");
 }
 cough(3);
}

void cough(int x)
{
 for (int i = 0; i < 3; i ++)
 {
  printf("Cough\n");
 }
}

#include <stdio.h>
int main() {
 int num = 5;
 int *ptr = &num;
 printf("%p\n", &ptr);
 printf("%p\n", ptr);
 printf("%d\n", *ptr);
}

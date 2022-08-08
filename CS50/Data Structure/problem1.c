#include <stdio.h>
typedef struct{
 int km;
 int kph;
 int kg;
 } car;
int main(void){
 car audi = {12000, 230, 760};
 car *ptr = &audi;
 printf("%d\n", (*ptr).km);
 printf("%d\n", ptr->km);
 printf("%d\n", audi.km);
}

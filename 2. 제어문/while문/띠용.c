#include<stdio.h>

int main(void)
{

int a = 1, cnt = 1, max = 2;
 
while(cnt == 100)
{
    max = max + a;
    cnt = cnt + 1;
    a = a + 1;
}

printf("1 ~ 100까지의 총 합은 %d이다", a);
}

#include <stdio.h>

int main()
{
	int a, sum, i;
	
	for(i = 1; i <= 100;i++)
	{
		if(i % 3 == 0)
			sum += i;
	}
	printf("%d", sum);
}

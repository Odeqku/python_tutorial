#include <stdio.h>

int power(int x, int n);

void main()
{
	int v = 10;
	int x = 2;
	int result;

	result = power(x, v);
        printf("\n%d\n", result);


}

int power(int x, int n)
{
	printf("%d\n", n);
	if (n == 0)
		return 1;
	int temp = power(x, n/2);

	printf("(x:%d, n:%d, temp:%d)\n", x,  n, temp);
	
	if (n % 2 == 0)
		return temp * temp;
	else
		return x * temp * temp;
}

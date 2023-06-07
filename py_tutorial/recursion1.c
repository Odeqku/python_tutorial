#include <stdio.h>


int display(int n)
{
	if (n == 96)
		return 97;
	else
	{
		display(n - 2);
		printf("%c", n);
	}
}

void main()
{
	int n = 122;
	int p = display(n);
}

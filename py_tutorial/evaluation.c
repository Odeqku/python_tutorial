#include <stdio.h>


int main(void)
{
	int i;
	int j;

	for (i = 0; i < 10; i++)
	{
		j = 0;
		while (j < 10)
		{
			printf("%d", j);
			j++;
		}

		printf("\n");
	}
	return (0);
}

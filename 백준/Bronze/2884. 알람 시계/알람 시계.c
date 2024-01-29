#include <stdio.h>

int main()
{
	int H, M;
	scanf(" %d %d", &H, &M);

	if (H == 0)
	{
		if (M == 0)
			printf("23 15");
		else if (M < 45)
			printf("23 %d", 15 + M);
		else
			printf("0 %d", M-45);
	}
	else
	{
		if (M == 0)
			printf("%d 15", H-1);
		else if (M < 45)
			printf("%d %d", H - 1, 15+ M);
		else
			printf("%d %d", H, M - 45);
	}
}
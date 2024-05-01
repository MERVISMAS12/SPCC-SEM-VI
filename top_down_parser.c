#include<stdio.h>
// S->aAb | c
// A->cd | d
void main()
{
	char inp[10];
	printf("Enter string: ");
	scanf("%s", inp);
	int i = 0;
	int A(char x)
	{
		if(x == 'c')
		{
			if(inp[++i] == 'd')
				return 1;
		}
		if(x == 'd')
			return 1;
		else
			return 0;
	}
	int S(char x)
	{
		if(x == 'a')
		{
			if(A(inp[++i]))
			{
				if(inp[++i] == 'b' && inp[i+1] == '\0')
					return 1;
				return 0;	
			}
			return 0;
		}
		else if(x == 'c' && inp[i+1] == '\0')
			return 1;
		else
			return 0;	
	}
	
	if(S(inp[i]))
		printf("Successful");
	else
		printf("error");
}

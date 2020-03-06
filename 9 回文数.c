#include<stdio.h>
#include <stdlib.h>

int reverge(int x)
{
int rev = 0;
		while (x != 0)
		{
			int pop = x % 10; 
			x /= 10;
			if (rev > INT_MAX / 10) 
			{
				return 0;
			}
			if (rev < INT_MIN / 10)
			{
				return 0;
			}
			rev = rev * 10 + pop;
		}

		return rev;
}
int main(int arg, char *argv[])
{
    int input = atoi(argv[1]);
    int e = reverge(input);
    if(reverge == e)
    {
        return true;
    }
    return false;

}
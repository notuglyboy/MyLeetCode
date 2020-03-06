#include<stdio.h>
#include <stdlib.h>

#define INT_MAX 2147483647
#define INT_MIN -2147483648
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


int reverse_my(int x) {
	int tmp = x;
	int tail = tmp%10;
	int re = tmp/10;
	int sign = 1;
	int result = 0;
	if(tmp < 0) {
		if((re == -INT_MAX/10 & tail < -8)||(re<-INT_MAX /10))
		            return 0;
		sign = -1;
		tmp = -tmp;
	}
	if((re == INT_MAX/10 & tail > 7)||(re>INT_MAX/10))
	            return 0;
	while(tmp>0) {
		int tail = tmp%10;
		result = result*10 + tail;
		tmp = tmp / 10;
	}
	return result*sign;
} 
int main(int arg, char *argv[])
{
    int input = atoi(argv[1]);
    int e = reverse_my(input);
    printf("result is %d, %d", e, input);

}
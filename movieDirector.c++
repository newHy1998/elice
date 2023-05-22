#include <iostream>
#include <cstdlib>
#include <cstring>
#include <sstream>
using namespace std;

int main(void)
{
	int data = 0;
	int data2 = 0;
	int flowcount = 665;
	int count = 0;
	int result = 0;
	string dat;

	cin >> data;

	while (1)
	{
		if (count == data)
		{
			break;

		}

		dat = to_string(flowcount);

		if (dat.find("666") != string::npos)
		{
			result = flowcount;
			count++;
			flowcount++;

		}
		else
		{
			flowcount++;
			continue;

		}

	}

	printf("%d \n", result);

}
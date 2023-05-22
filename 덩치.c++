#include <iostream>
#include <cstdlib>

using namespace std;

class person
{
private:
	int kg;
	int height;
	int result;

public:
	person()
	{
		kg = 0;
		height = 0;
		result = 1;

	}
	int getkg()
	{
		return kg;

	}
	int getheight()
	{
		return height;

	}
	int getresult()
	{
		return result;

	}
	void initdata(int kg1, int height1)
	{
		kg = kg1;
		height = height1;

	}
	void initresult()
	{
		result++;

	}

};
int main(void)
{
	person plist[50];
	int data;
	int kg;
	int height;
	int score;

	cin >> data;

	for (int i = 0; i < data; i++)
	{
		cin >> kg >> height;
		plist[i].initdata(kg, height);

	}

	for (int i = 0; i < data; i++)
	{
		for (int j = 0; j < data; j++)
		{
			if (i == j)
			{
				continue;
				
			}

			if (plist[i].getkg() < plist[j].getkg() && plist[i].getheight() < plist[j].getheight())
			{
				plist[i].initresult();

			}

		}

	}

	for (int i = 0; i < data; i++)
	{
		int result = plist[i].getresult();
		printf("%d ", result);

	}

}
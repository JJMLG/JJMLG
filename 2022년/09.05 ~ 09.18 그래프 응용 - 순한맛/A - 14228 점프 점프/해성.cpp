#include <iostream>
#include <queue>
#define MAXD (100000)
using namespace std;
struct STATUS
{
	int dis;
	int cnt;
};
int N, S;
queue<STATUS>Q;
int pos[] = { -1,1 };
int arr[MAXD + 10];
int record[MAXD + 10];
int result = 0;
void input(void)
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}
	cin >> S;
}
int BFS()
{
	Q.push({ S,0 });
	//방문
	while (!Q.empty())
	{
		STATUS DATA = Q.front(); Q.pop();
		for (int i = 0; i < N; i++)
		{
			for (int c = 0; c < 1; c++)
			{
				STATUS NEWD;
				NEWD.dis = DATA.dis + (arr[i] * (pos[c]));
				if (NEWD.dis<1 || NEWD.dis > N) continue;
				if (!record[NEWD.dis]) result++;
				record[NEWD.dis] = 1;
				NEWD.cnt = DATA.cnt + 1;
				Q.push(NEWD);
			}
		}
	}
	cout << result;
}
int main(void)
{
	input();
	BFS();
	return 0;
}

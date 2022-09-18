#include <iostream>
#include <queue>
using namespace std;
int M, N;
int tomato_box[1000 + 2][1000 + 2];
int changeTime = 0;
struct ST
{
	int r, c, days;
};
queue<ST> Q;
void inputData()
{
	cin >> M >> N;
	for (int r = 0; r < N; r++)
	{
		for (int c = 0; c < M; c++)
		{
			cin >> tomato_box[r][c];
		}
	}
}

void BFS()
{
	static int dr[] = { -1,0,1,0 };
	static int dc[] = { 0,1,0,-1 };
	for (int r = 0; r < N; r++)
	{
		for (int c = 0; c < M; c++)
		{
			if (tomato_box[r][c] == 1)
			{
				Q.push({ r,c,1 });
			}
		}
	}
	while (!Q.empty())
	{
		ST data = Q.front(); Q.pop();
		for (int i = 0; i < 4; i++)
		{
			ST newdata = data;
			newdata.r += dr[i];
			newdata.c += dc[i];
			if (newdata.r < 0 || newdata.c < 0 || newdata.r >= N || newdata.c >= M) continue;
			if (tomato_box[newdata.r][newdata.c]) continue;
			tomato_box[newdata.r][newdata.c] = newdata.days;
			newdata.days += 1;
			Q.push(newdata);
		}
	}
}
int checkSuccess()
{
	for (int r = 0; r < N; r++)
	{
		for (int c = 0; c < M; c++)
		{
			if (changeTime < tomato_box[r][c]) changeTime = tomato_box[r][c];
			if (!tomato_box[r][c]) return 0;
		}
	}
	return 1;
}
int main(void)
{
	inputData();
	BFS();
	if (!checkSuccess()) cout << -1;
	else if (changeTime == 1)cout << 0;
	else cout << changeTime;
	return 0;
}
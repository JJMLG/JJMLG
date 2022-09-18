#include <iostream>
#include <vector>
using namespace std;
int H, W;
int arr[100 + 2][100 + 2];
int times = 0;
int ans = 0;
int result;
void inputData() 
{
	cin >> H >> W;
	for (int r = 0; r < H; r++) 
	{
		for (int c = 0; c < W; c++) 
		{
			cin >> arr[r][c];
		}
	}
}
void DFS(int r, int c) 
{
	static int dr[] = { -1,0, 1,0 };
	static int dc[] = { 0, 1,0 ,-1 };
	arr[r][c] = 2;

	for (int i = 0; i < 4; i++) 
	{
		int dy = r + dr[i];
		int dx = c + dc[i];
		if (dy < 0 || dx < 0 || dy >= H || dx >= W) continue;
		if (arr[dy][dx] == 2) continue;
		else if (arr[dy][dx] == 0) DFS(dy, dx);
		else if (arr[dy][dx] == 1) arr[dy][dx] = 2;
	}
}
int check() 
{
	int cnt = 0;
	for (int r = 0; r < H; r++)
	{
 		for (int c = 0; c < W; c++) 
		{
			if (arr[r][c] == 1) cnt++;
		}
	}
	for (int r = 0; r < H; r++)
	{
		for (int c = 0; c < W; c++)
		{
			if (arr[r][c] == 2) arr[r][c] = 0;
		}
	}
	return cnt;
}
int solve()
{
	int remain = check();
	result = remain;
	for (int r = 0; r < H; r++)
	{
		for (int c = 0; c < W; c++)
		{
			if (arr[r][c]==2)continue;
			DFS(r, c);
			times++;
			remain = check();
			if (!remain) return 1;
			result = remain;
		}
	}	
	return 1;
}
int main(void)
{
	inputData();
	solve();
	cout << times << '\n' << result;
	return 0;
}
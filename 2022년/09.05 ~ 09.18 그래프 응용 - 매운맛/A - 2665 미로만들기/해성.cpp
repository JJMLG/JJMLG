#include <iostream>
#include <queue>
#define MAX_n (50)
using namespace std;
int n;
struct ST
{
	int r, c, cnt;
};
queue<ST> Q;
char arr[MAX_n + 2][MAX_n + 2];
int check[MAX_n + 2][MAX_n + 2];
void inputData(void) 
{
	cin >> n;
	for (int r = 1; r <= n; r++) 
	{
		for (int c = 1; c <= n; c++) 
		{
			cin >> arr[r][c];
			
		}
	}
	fill(&check[0][0], &check[n+1][n+1], 0x7ffffff);
}

int BFS() 
{
	static int dr[] = { -1,0,1,0 };
	static int dc[] = { 0,1,0,-1 };
	Q.push({ 1,1,0 });
	check[1][1] = 0;
	while (!Q.empty()) 
	{
		ST DATA = Q.front(); Q.pop();
		for (int i = 0; i < 4; i++) 
		{
			ST newdata = DATA;
			newdata.r += dr[i];
			newdata.c += dc[i];
			if (newdata.r<1 || newdata.c<1 || newdata.r > n || newdata.c>n) continue;
			if (arr[newdata.r][newdata.c] == '0') newdata.cnt += 1;
			if (check[newdata.r][newdata.c] <= newdata.cnt) continue;
			if (check[newdata.r][newdata.c] > newdata.cnt) 
			{
				check[newdata.r][newdata.c] = newdata.cnt;
				Q.push(newdata);
			}
		}
	}
	return check[n][n];
}
int main(void) 
{
	inputData();
	cout << BFS();

	return 0;
}
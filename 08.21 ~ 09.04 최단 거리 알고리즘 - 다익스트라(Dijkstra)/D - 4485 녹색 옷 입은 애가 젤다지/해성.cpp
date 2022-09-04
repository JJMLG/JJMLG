#include <iostream>
#include <vector>
#include <queue>
#define INF (1e9)
int N;
int cnt = 1;
std::vector<std::vector<int>> arr(125 + 10, std::vector<int>(125 + 10));
std::vector<std::vector<int>>d(125 + 10, std::vector<int>(125 + 10));
int visited[125 + 10][125 + 10];
int Y[] = { 0, 1, 0 ,-1 };
int X[] = { 1, 0,-1,0 };

void input(void)
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			int numb;
			std::cin >> numb;
			arr[i][j] = numb;
		}
	}
}
void init(void)
{
	for (int i = 0; i <= N; i++)
	{
		for (int j = 0; j <= N; j++)
		{
			arr[i][j] = 0;
			d[i][j] = INF;
			visited[i][j] = 0;
		}
	}
}
void solve(void)
{
	std::priority_queue<std::vector<int>> PQ;
	d[0][0] = arr[0][0];
	PQ.push({ arr[0][0] ,0, 0, });
	while (!(PQ.empty()))
	{
		int currentY = PQ.top()[1];
		int currentX = PQ.top()[2];
		int current_cost = d[currentY][currentX];
		PQ.pop();
		for (int i = 0; i < 4; i++)
		{
			int dy = currentY + Y[i];
			int dx = currentX + X[i];
			if (dy<0 || dx<0 || dy>N - 1 || dx>N - 1) continue;
			if (d[dy][dx] < current_cost) continue;
			if (d[dy][dx] > arr[dy][dx] + current_cost)
			{
				d[dy][dx] = arr[dy][dx] + current_cost;
				PQ.push({ -d[dy][dx],dy, dx });
			}
		}
	}
	std::cout << "Problem " << cnt << ": " << d[N - 1][N - 1] << '\n';
	cnt++;

}
int main(void)
{
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);
	std::cout.tie(0);
	while (1)
	{
		std::cin >> N;

		if (N == 0) break;
		init();
		input();
		solve();
	}
}
#include <iostream>
#include<vector>
#include<queue>
#define INF 1E9
int N, M;
int start, destination;
std::vector<std::pair<int, int>> arr[1000 + 10];
int d[1000 + 10];
void input(void)
{
	std::cin >> N >> M;
	for (int i = 0; i < M; i++)
	{
		int from, to, value;
		std::cin >> from >> to >> value;
		arr[from].push_back({ value,to });
	}
	std::cin >> start >> destination;
}
void distance_init()
{
	for (int i = 1; i <= N; i++)
	{
		d[i] = INF;
	}
}
void dijkstra(int ST)
{
	d[ST] = 0;
	std::priority_queue<std::pair<int, int>> PQ;
	PQ.push({ 0,ST });
	while (!(PQ.empty()))
	{
		int c_cost = -PQ.top().first;
		int c = PQ.top().second;
		PQ.pop();

		if (d[c] < c_cost) continue;
		for (int i = 0; i < arr[c].size(); i++)
		{
			int n_cost = arr[c][i].first;
			int next = arr[c][i].second;
			if (d[next] > n_cost + c_cost)
			{
				d[next] = n_cost + c_cost;
				PQ.push({ -d[next], next });
			}
		}
	}
}
void solve(void)
{
	dijkstra(start);
	std::cout << d[destination];
}
int main()
{
	input();
	distance_init();
	solve();
}
#include <iostream>
#include <vector>
#include <queue>
#define INF 1e9
using namespace std;
int V, E, K;
vector<pair<int, int>> arr[20000 + 10];
int D[20000 + 10];
priority_queue<pair<int, int>> pq;
void input(void)
{
	cin >> V >> E >> K;

	for (int i = 0; i < E; i++)
	{
		int u, v, w; cin >> u >> v >> w;
		arr[u].push_back({ w, v });
	}
}
void init(void)
{
	for (int i = 1; i <= V; i++)
	{
		D[i] = INF;
	}
}
void dijkstra(int start)
{
	D[start] = 0;
	pq.push({ 0, start });
	while (!pq.empty())
	{
		int nowvalue = -(pq.top().first);
		int nowpos = pq.top().second;
		pq.pop();

		if (D[nowpos] < nowvalue) continue;
		int lens = arr[nowpos].size();
		for (int i = 0; i < lens; i++)
		{
			int nextvalue = arr[nowpos][i].first;
			int next = arr[nowpos][i].second;

			if ((nextvalue + nowvalue) < D[next])
			{
				D[next] = nextvalue + nowvalue;
				pq.push({ -D[next], next });
			}
		}
	}
	for (int i = 1; i <= V; i++)
	{
		if (D[i] == (int)INF)
		{
			cout << "INF" << '\n';
		}
		else cout << D[i] << '\n';
	}
}
int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	init();
	dijkstra(K);
	return 0;
}

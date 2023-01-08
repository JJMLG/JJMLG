#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#define INF (int)1e9
using namespace std;

int N, M, K, X;
vector<pair<int, int>> arr[300000 + 10];
priority_queue<pair<int, int>> pq;
int D[300000 + 10] = { 0 };
void input(void)
{
	memset(arr, 0, sizeof(arr));
	cin >> N >> M >> K >> X;
	for (int i = 0; i < M; i++)
	{
		int start, to; cin >> start >> to;
		arr[start].push_back({ 1, to });
	}
}
void init(void)
{
	//거리정보 초기화
	for (int i = 1; i <= N; i++)
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
		int current_value = -(pq.top().first);
		int current_position = pq.top().second;
		pq.pop();
		if (D[current_position] < current_value) continue;
		int lens = arr[current_position].size();
		for (int i = 0; i < lens; i++)
		{
			int destination_value = arr[current_position][i].first;
			int destination_position = arr[current_position][i].second;

			if (D[destination_position] > current_value + destination_value)
			{
				D[destination_position] = current_value + destination_value;
				pq.push({ -(D[destination_position]), destination_position });
			}
		}
	}
	int isk = false;
	for (int i = 1; i <= N; i++)
	{
		if (D[i] == K)
		{
			cout << i << '\n';
			isk = true;
		}
	}
	if (!isk) cout << -1;

}
int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	init();
	dijkstra(X);
	return 0;
}
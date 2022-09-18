#include <iostream>
using namespace std;
#include <vector>
#include <queue>

int N, K;
int visit[100 + 1];
vector<vector<int>> arr(100+1);
queue<int> Q;
void inputData() 
{
	cin >> N >> K;
	for (int i = 0; i < K; i++) 
	{
		int s, e; cin >> s >> e;
		arr[s].push_back(e);
		arr[e].push_back(s);
	}
}
void BFS(int node) 
{
	fill(visit, visit + 101, 0);
	Q = {};
	visit[node] = 1;
	Q.push(node);
	while (!Q.empty()) 
	{
		int now = Q.front(); Q.pop();
		int lens = arr[now].size();
		for (int i = 0; i < lens; i++) 
		{
			if (visit[arr[now][i]]) continue;
			visit[arr[now][i]] = 1;
			visit[arr[now][i]] = visit[now] + 1;
			Q.push(arr[now][i]);
		}
	}
}
int solve() 
{
	for (int i = 1; i <= N; i++) 
	{
		BFS(i);
		for (int j = 1; j <= N; j++) 
		{
			if (!visit[j] || visit[j] > 6) return 0;
		}
	}
	return 1;
}
int main(void) 
{
	inputData();
	if (solve()) cout << "Small World!";
	else cout << "Big World!";
	return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAXN (10000)
int N, M;
vector<int> adjlist[MAXN + 1];
int visit[MAXN + 1];
int cnt, maxnode, maxx;
vector<int> result;
void DFS(int node) {
	visit[node] = 1;
	cnt++;
	for (int i = 0; i < adjlist[node].size(); i++) {
		int next = adjlist[node][i];
		if (visit[next]) continue;
		DFS(next);
	}
}
void print(int node) {
	cout << node<< " ";
	visit[node] = 1;
	for (int i = 0; i < adjlist[node].size(); i++) {
		int next = adjlist[node][i];
		if (visit[next]) continue;
		print(next);
	}
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		int a, b; cin >> a >> b;
		adjlist[b].push_back(a);
	}
	for (int i = 1; i <= N; i++) {
		fill(&visit[1], &visit[N + 1], 0);
		cnt = 1;
		DFS(i);
		if (cnt > maxx) {
			result.clear();
			maxnode = i;
			maxx = cnt;
			result.push_back(i);
		}
		else if (cnt == maxx) {
			result.push_back(i);
		}
	}
	for (auto i : result) cout << i << " ";
	return 0;
}
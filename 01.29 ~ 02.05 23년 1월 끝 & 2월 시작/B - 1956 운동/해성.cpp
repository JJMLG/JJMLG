#include <iostream>
#include <algorithm>
using namespace std;
#define MAX_V (400)
#define INF (0x7ffffff)
int V, E;
int adjMatrix[MAX_V + 2][MAX_V + 2];
void input() {
	cin >> V >> E;
	fill(&adjMatrix[0][0], &adjMatrix[V][V+1], INF);
	for (int i = 0; i < E; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		adjMatrix[a][b] = c;
	}
	for (int i = 1; i <= V; i++) {
		for (int h = 1; h <= V; h++) {
			if (i==h) adjMatrix[i][h] = 0;
		}
	}
}
int solve() {
	for (int mid = 1; mid <= V; mid++) {
		for (int node = 1; node <= V; node++) {
			for (int nextNode = 1; nextNode <= V; nextNode++) {
				adjMatrix[node][nextNode] = min(adjMatrix[node][nextNode], adjMatrix[node][mid] + adjMatrix[mid][nextNode]);
			}
		}
	}
	int minn = INF;
	for (int node = 1; node <= V; node++) {
		for (int nextNode = 1; nextNode <= V; nextNode++) {
			if (node == nextNode) continue;
			minn = min(minn, adjMatrix[node][nextNode] + adjMatrix[nextNode][node]);
		}
	}
	if (minn == INF) return -1;
	return minn;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	input();
	cout << solve() <<'\n';
	return 0;
}
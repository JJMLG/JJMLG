#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define MAX_SIZE (100000)
struct ST {
	int d, cnt;
};
struct COMP {
	bool operator()(ST a, ST b) {
		return a.cnt > b.cnt;
	}
};
int N, K;
int visit[MAX_SIZE + 2];
int BFS() {
	if (N == K) return 0;
	fill(&visit[0], &visit[MAX_SIZE + 1], 0xf777777);
	priority_queue<ST, vector<ST>, COMP>q;
	q.push({ N,0 });
	visit[N] = 0;
	while (!q.empty()) {
		ST data = q.top(); q.pop();
		if (data.d == K) return visit[data.d];
		for (int i = 0; i < 3; i++) {
			ST newdata = data;
			if (i == 0) {
				newdata.d -= 1;
				newdata.cnt++;
			}
			else if (i == 1) {
				newdata.d += 1;
				newdata.cnt++;
			}
			else {
				newdata.d *= 2;
			}
			if (newdata.d < 0 || newdata.d > MAX_SIZE) continue;
			if (visit[newdata.d] > newdata.cnt) visit[newdata.d] = newdata.cnt;
			else continue;
			q.push(newdata);
		}
	}
}
int main() {
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> N >> K;
	cout << BFS() << '\n';
	return 0;
}

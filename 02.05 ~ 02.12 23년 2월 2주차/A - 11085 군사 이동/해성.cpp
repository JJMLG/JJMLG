//다시 풀어봐야 할 문제 거의 정답코드 보고 이해함
//https://travelbeeee.tistory.com/364
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define MAX_P (1000)

struct ST {
	int s, e, val;
};
struct COMP {
	bool operator ()(ST a, ST b) {
		return a.val < b.val;
	}
};
priority_queue<ST,vector<ST>, COMP> pq;

int par[MAX_P + 1];
int P, W, C, V;

void input() {
	cin >> P >> W >> C >> V;
	for (int i = 0; i < W; i++) {
		int s, e, w;
		cin >> s >> e >> w;
		pq.push({ s,e,w });
	}
}
//최상위 부모 찾기
int find_parent(int x){
	if (par[x] == x) return x;
	return par[x] = find_parent(par[x]);
}
// 집합 합치기
void unions(int x, int y) {
	int p_x = find_parent(x);
	int p_y = find_parent(y);
	// 부모가 작은 쪽으로 다 합치기
	if (p_x < p_y) par[p_y] = p_x;
	else if(p_x>p_y) par[p_x] = p_y;
}
void solve() {
	for (int i = 0; i < P; i++) {
		par[i] = i;
	}
	while (!pq.empty()) {
		int s = pq.top().s;
		int e = pq.top().e;
		int val = pq.top().val;
		pq.pop();
		//일단 경로 잇기 == 한 집합에 두기 == 한 루트 부모에 두기
		unions(s, e);
		//만약에 출발지랑 도착지 부모가 같다면, 즉 같은 집합이면 끝내기
		if (find_parent(C) == find_parent(V)) {
			cout << val;
			break;
		}
	}
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	input();
	solve();
	return 0;
}
//#include <iostream>
//#include <vector>
//#include <algorithm>
//using namespace std;
//#define MAX_P (1000)
//vector<int> path;
//vector<vector<int>> allPath;
//
//int adjArr[MAX_P + 1][MAX_P + 1];
//vector<int> adjlist[MAX_P + 1];
//int visit[MAX_P + 1];
//int P, W, C, V;
//
//void input() {
//	cin >> P >> W >> C >> V;
//	for (int i = 0; i < W; i++) {
//		int s, e, w;
//		cin >> s >> e >> w;
//		adjArr[s][e] = w;
//		adjArr[e][s] = w;
//		adjlist[s].push_back(e);
//		adjlist[e].push_back(s);
//	}
//}
//int maxx=0;
//void DFS(int node, int val) {
//	if (node == V) {
//		for (auto i : path) cout << i << " ";
//		cout <<"val : " << val << '\n';
//		if (val > maxx) maxx = val;
//		return;
//	}
//	for (int c = 0; c < adjlist[node].size(); c++) {
//		int next = adjlist[node][c];
//		if (visit[next]) continue;
//		visit[next] = 1;
//		path.push_back(next);
//		DFS(next,min(val, adjArr[node][next]));
//		visit[next] = 0;
//		path.pop_back();
//	}
//	return;
//}
//int main(void) {
//	input();
//	visit[C] = 1;
//	DFS(C, 0x7ffffff);
//	return 0;
//}
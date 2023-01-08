#define _CRT_SECURE_NO_WARNINGS
#if 1
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_N (100000)
int T, N;
int visit[MAX_N + 2];
int finished[MAX_N + 2];
int adj[MAX_N+2];
int gcnt;
void input() {
	cin >> N;
	fill(&adj[1], &adj[MAX_N+1], 0);

	for (int i = 1; i <= N; i++) {
		cin >> adj[i];
	}
}

void DFS(int node) {
	visit[node] = 1;
	int next = adj[node];
	if (!visit[next]) {
		DFS(next);
	}
	else {
		if (!finished[next]) {
			gcnt++;
			for (int i = next; i != node; i = adj[i]) {
				if(!finished[i]) finished[i]= 1;
				gcnt++;
			}
		}
	}
	finished[node] = 1;
}
void solve() {
	fill(&finished[1], &finished[MAX_N+1], 0);
	fill(&visit[1], &visit[MAX_N+1], 0);
	gcnt = 0;
	for (int i = 1; i <= N; i++) {
		if (visit[i]) continue;
		if (visit[adj[i]]) continue;
		DFS(i);
	}
	cout << N-gcnt << '\n';
}
int main(void) {
	freopen("termproject.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		input();
		solve();
	}
	return 0;
}

#endif

#if 0
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
#define MAX_N (100000)

int T, N, cnt;
int adjlist[MAX_N + 2];
int visit[MAX_N + 2];
int finished[MAX_N + 2];
vector<int> groups;
void init() {
	fill(&visit[1], &visit[MAX_N + 1], 0);
	fill(&finished[1], &finished[MAX_N + 1], 0);
	groups.clear();
}

void input() {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		int cc; cin >> cc;
		adjlist[i] = cc;
	}
}
void DFS(int now) {
	visit[now] = 1;
	int next = adjlist[now];
	if (!visit[next]) DFS(next);
	else {
		if (!finished[next]) {
			cnt++;
			finished[now] = 1;
			for (int i = next; i != now; i = adjlist[i]) {
				cnt++;
				finished[i] = 1;
			}
		}
	}
	//visit[now] = 1;
	//int next = adjlist[now];
	//if (!visit[next]) DFS(next);
	////방문했는데 처리안되어 있으면
	//else if (!finished[next]){
	//	cnt++; // now포함해야하니까
	//	for (int i = next; i != now; i = adjlist[i]) {
	//		cnt++;
	//		finished[i] = 1;
	//	}
	//}
	//finished[now] = 1;
}
void solve() {
	cnt=0;
	for (int i = 1; i <= N; i++) {
		if (visit[i]) continue; 
		DFS(i);
	}
	cout << N - cnt << '\n';
}
int main(void) {
	freopen("termproject.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		init();
		input();
		solve();
	}
	return 0;
}
#endif
#if 0
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define MAX_N (100000)

int T, N, totalcnt;
int adjlist[MAX_N + 2];
vector<int> group[MAX_N + 2];
int visit[MAX_N + 2];
vector<int> groups;
int cnt, groupN;
void init() {
	for (int i = 0; i <= MAX_N; i++) {
		group[i].clear();
	}
	fill(&visit[1], &visit[MAX_N + 1], 0);
}

void input(){
	cin >> N;
	totalcnt = N;
	for (int i = 1; i <= N; i++) {
		int cc; cin >> cc;
		adjlist[i] = cc;
	}
}
void DFS(int now,int start) {
	if (visit[now]) return;
	visit[now] = 1;
	groups.push_back(now);
	int next = adjlist[now];
	if (next == now) { // 만약 다음숫자가 나라면 해당 숫자만 넣는다
		group[groupN].push_back(now);
		cnt++;
		groupN++;
		return;
	}
	if (groups.size()>1 && start == next) {
		for(int i=0; i< groups.size();i++){
			group[groupN].push_back(groups[i]);
			cnt++;
		}
		groupN++;

		return;
	}
	DFS(next, start);
}
void solve() {
	groupN = 1;
	cnt = 0;
	for (int i = 1; i <= N; i++) {
		if (visit[i]) continue;
		groups.clear();
		DFS(i, i);
	}
	for (int i = 1; i < groupN; i++) {
		cout << "#" << i << '\n';
		for (int j = 0; j < group[i].size(); j++) {
			cout << group[i][j] << " ";
		}
		cout << '\n';
	}
}
int main(void) {
	freopen("termproject.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		init();
		input();
		solve();
		//cout << totalcnt-cnt << '\n';
	}
	return 0;
}
#endif

#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
#define MAX_N (50)
int N, M;
struct POS {
	int r, c;
};
struct VI {
	int r, c, times;
};
vector<POS> viruses;
vector<vector<int> > virus_comb;
vector<int> comb_sub;
queue<VI> q;
POS D[] = { {-1,0},{0,1},{1,0},{0,-1} };
int visit[MAX_N + 2][MAX_N + 2];
int maps[MAX_N + 2][MAX_N + 2];
int record_maps[MAX_N + 2][MAX_N + 2];
int totalblank;
void input() {
	cin >> N >> M;
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			cin >> maps[r][c];
			if (maps[r][c] == 2) {
				viruses.push_back({ r,c });
			}
			else if (maps[r][c] == 0) totalblank++;
		}
	}
}
void DFS(int start, int cnt) {
	if (cnt == M) {
		virus_comb.push_back(comb_sub);
		return;
	}
	for (int i = start; i < viruses.size(); i++) {
		comb_sub.push_back(i);
		DFS(i + 1, cnt + 1);
		comb_sub.pop_back();
	}
}
int Allcheck() {
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			if (!maps[r][c]) return 0; // 하나라도 0이면
		}
	}
	return 1;
}
int floodfill(int combidx) {
	fill(&visit[0][0], &visit[MAX_N + 1][MAX_N + 2],0);
	copy(&maps[0][0], &maps[MAX_N + 1][MAX_N + 2], &record_maps[0][0]);
	q = {};
	int maxx = 0;
	int ret= Allcheck();
	if (ret) return 0;
	for (int i = 0; i < virus_comb[combidx].size(); i++) {
		int virusidx = virus_comb[combidx][i];
		q.push({ viruses[virusidx].r, viruses[virusidx].c, 0 });
		visit[viruses[virusidx].r][viruses[virusidx].c] = 1;
	}
	int blank = 0;
	while (!q.empty()) {
		VI data = q.front(); q.pop();
		for (int i = 0; i < 4; i++) {
			VI ndata = data;
			ndata.r += D[i].r;
			ndata.c += D[i].c;
			ndata.times += 1;
			if (visit[ndata.r][ndata.c]) continue;
			if (ndata.c < 0 || ndata.r < 0 || ndata.c >= N || ndata.r >= N) continue;
			if (record_maps[ndata.r][ndata.c] == 1) continue; // 벽이면 가면안되니까
			if (record_maps[ndata.r][ndata.c] == 0 ) blank++;
			visit[ndata.r][ndata.c] = ndata.times;
			q.push(ndata);
			if (maxx < ndata.times) maxx = ndata.times;
			if (blank == totalblank) return maxx;
		}
	}
	return -1;
}
void print() {
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			cout << record_maps[r][c] << " ";
		}
		cout << '\n';
	}
	cout << '\n';
}

int simulation() {
	int mintimes = 0xf777777;
	DFS(0, 0);
	for (int i = 0; i < virus_comb.size(); i++) {
		int temp = floodfill(i);
		if (temp == -1) continue;
		if (temp < mintimes) mintimes = temp;
		//print();
	}
	if (mintimes == 0xf777777) return -1;
	return mintimes;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	input();
	cout << simulation() << '\n';

	return 0;
}
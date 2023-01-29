#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAX_WH (100)
int W, H;
int maps[MAX_WH + 2][MAX_WH + 2];
int visit[MAX_WH + 2][MAX_WH + 2];

struct POS {
	int r, c;
};
POS DIR[2][6] = { 
	{ {0,-1}, {-1,-1},{-1,0},{0,1},{1,0},{1,-1} },
	{ {-1,0}, {-1,1},{0,1},{1,1},{1,0},{0,-1} } 
};
queue<POS> q;
void input() {
	cin >> W >> H;
	for (int r = 1; r <= H; r++) {
		for (int c = 1; c <= W; c++) {
			cin >> maps[r][c];
		}
	}
}
void makeSide() {
	q = {};
	q.push({ 0,0 });
	while (!q.empty()) {
		POS data = q.front(); q.pop();
		for (int idx = 0; idx < 6; idx++) {
			POS newdata = data;
			if (newdata.r % 2) {
				newdata.r += DIR[1][idx].r;
				newdata.c += DIR[1][idx].c;
			}
			else {
				newdata.r += DIR[0][idx].r;
				newdata.c += DIR[0][idx].c;
			}
			if (newdata.r < 0 || newdata.c < 0 || newdata.r > H + 1 || newdata.c > W + 1) continue;
			//if (visit[newdata.r][newdata.c]) continue;
			//visit[newdata.r][newdata.c] = 1;
			if (maps[newdata.r][newdata.c]) continue;
			maps[newdata.r][newdata.c] = 2;
			q.push(newdata);
		}
	}
}
//int isInRound(int r, int c) {
//	for (int idx = 0; idx < 6; idx++) {
//		int dy, dx;
//		if (r % 2) {
//			dy = r + DIR[1][idx].r;
//			dx = c + DIR[1][idx].c;
//		}
//		else {
//			dy = r + DIR[0][idx].r;
//			dx = c + DIR[0][idx].c;
//		}
//
//		if (dy < 1 || dx < 1 || dy > H || dx > W) return 0;
//		if (!maps[dy][dx]) return 0;
//	}
//	return 1;
//}
void makeMap() {
	for (int r = 0; r <= H+1; r++) {
		for (int c = 0; c <= W+1; c++) {
			if (maps[r][c] == 0) maps[r][c] = 1;
			//int ret = isInRound(r, c);
			/*if (ret) {
				maps[r][c] = 1;
			}*/
		}
	}
}
int checkNear(int r, int c) {
	int cnt = 0;
	for (int idx = 0; idx < 6; idx++) {
		int dy, dx;
		if (r % 2) {
			dy = r + DIR[1][idx].r;
			dx = c + DIR[1][idx].c;
		}
		else {
			dy = r + DIR[0][idx].r;
			dx = c + DIR[0][idx].c;
		}
		if (dy < 1 || dx < 1 || dy > H || dx > W) continue;
		if (maps[dy][dx]==1) cnt++;
	}
	return cnt;
}
void print() {
	cout << '\n';
	for (int r = 1; r <= H; r++) {
		for (int c = 1; c <= W; c++) {
			cout << maps[r][c] << " ";
		}
		cout << '\n';
	}
}
int calcCirm() {
	int total = 0;
	for (int r = 1; r <= H; r++) {
		for (int c = 1; c <= W; c++) {
			if (maps[r][c]==1) {
				int ret = checkNear(r,c);
				total += (6 - ret);
			};
		}
	}
	return total;
}

void printvisit() {
	for (int r = 0; r <= H + 1; r++) {
		for (int c = 0; c <= W + 1; c++) {
			cout << visit[r][c] << " ";
		}
		cout << '\n';
	}
}
void solve() {
	makeSide();
	makeMap();
	cout << calcCirm() << '\n';
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	input();
	solve();
	return 0;
}
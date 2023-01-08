#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX_AB (100)
#define MAX_M (100)
#define MAX_N (100)
struct ORD {
	int robotidx;
	int rep;
	char cmds;
};
struct POS {
	int r, c;
};
struct RB {
	int r, c, dir;
};
vector<ORD> orders;
RB robots[MAX_N + 1];
POS D[] = { {-1,0},{0,1},{1,0},{0,-1} };
int C, R, N, M;
int arr[MAX_AB + 2][MAX_AB + 2];
int maps[MAX_AB + 2][MAX_AB + 2];
void input() {
	cin >> C >> R >> N >> M;
	for (int i = 1; i <= N; i++) {
		int c, r; char dir; cin >> c >> r >> dir;
		robots[i].c = c;
		robots[i].r = R - r + 1;
		maps[robots[i].r][robots[i].c] = i;
		if (dir == 'N') robots[i].dir = 0;
		else if (dir == 'E') robots[i].dir = 1;
		else if (dir == 'S') robots[i].dir = 2;
		else robots[i].dir = 3;
	}
	for (int i = 0; i < M; i++) {
		int rbidx, repeat;
		char cmd;
		cin >> rbidx >> cmd >> repeat;
		orders.push_back({ rbidx,repeat, cmd });
	}
}
void init() {
	for (int i = 1; i <= MAX_N + 1; i++) {
		robots[i] = { 0,0,0 };
	}
	fill(&arr[0][0], &arr[MAX_AB + 1][MAX_AB + 2], 0);
	fill(&maps[0][0], &maps[MAX_AB + 1][MAX_AB + 2], 0);
}
int moveRobot(int rbidx, int rep, char cmd) {
	//움직이자
	int dy = robots[rbidx].r;
	int dx = robots[rbidx].c;
	int dir = robots[rbidx].dir;

	maps[dy][dx] = 0;//원래 자리 비우기

	for (int i = 1; i <= rep; i++) {
		if (cmd == 'L') {
			dir -= 1;
			if (dir < 0) dir = 3;
		}
		else if (cmd == 'R') {
			dir = (dir + 1) % 4;
		}
		else {
			dy += D[dir].r;
			dx += D[dir].c;
			if (maps[dy][dx]) return maps[dy][dx]; // 로봇이 있으면 충돌
			if (dy<1 || dx<1 || dy>R || dx>C) return -1; // 벽이면 
		}
	}
	robots[rbidx].r = dy;
	robots[rbidx].c = dx;
	robots[rbidx].dir = dir;
	maps[dy][dx] = rbidx;
	return 0;
}
void print() {
	for (int r = 1; r <= R; r++) {
		for (int c = 1; c <= C; c++) {
			cout << maps[r][c] << " ";
			if (robots[maps[r][c]].dir == 0) cout << "↑	 ";
			else if (robots[maps[r][c]].dir == 1) cout << "→	 ";
			else if (robots[maps[r][c]].dir == 2) cout << "↓	 ";
			else if (robots[maps[r][c]].dir == 3) cout << "←	 ";

		}
		cout << '\n';
	}
}
void solve() {
	for (int i = 0; i < M; i++) {
		int ret = moveRobot(orders[i].robotidx, orders[i].rep, orders[i].cmds);
		if (ret == -1) {
			cout << "Robot " << orders[i].robotidx << " crashes into the wall" << '\n';
			return;
		}
		else if (ret > 0) {
			cout << "Robot " << orders[i].robotidx << " crashes into robot " << ret << '\n';
			return;
		}
	}
	cout << "OK" << '\n';
	return;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	init();
	input();
	solve();

	return 0;
}
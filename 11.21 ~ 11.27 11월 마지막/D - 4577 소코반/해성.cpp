#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define MAX_RC (15)

struct POS {
	int r, c;
};
vector<int> orders;
struct ME {
	int r, c;
}me;

POS D[] = { {-1,0},{0,1},{1,0},{0,-1} };
int R, C;
char maps[MAX_RC + 1][MAX_RC + 1];
char origin_maps[MAX_RC + 1][MAX_RC + 1];

void init() {
	orders.clear();
	fill(&maps[0][0], &maps[MAX_RC][MAX_RC + 1], '#');
	me = { 0,0 };
}
int input() {
	cin >> R >> C;
	if (!R && !C) return 0;

	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			cin >> maps[r][c];
			origin_maps[r][c] = maps[r][c];
			if (maps[r][c] == 'w' || maps[r][c] == 'W') {
				me.r = r;
				me.c = c;
			}
		}
	}
	string cc; cin >> cc;
	for (int i = 0; i < cc.size(); i++) {
		if (cc[i] == 'U') orders.push_back(0);
		else if (cc[i] == 'R') orders.push_back(1);
		else if (cc[i] == 'D') orders.push_back(2);
		else if (cc[i] == 'L') orders.push_back(3);
	}
	return 1;
}
void move(int dir) {
	int dy = me.r + D[dir].r;
	int dx = me.c + D[dir].c;
	//벽이면
	if (maps[dy][dx] == '#') return;
	//박스라면 그 앞이 또 벽이나 박스라면
	else if (maps[dy][dx] == '.' || maps[dy][dx] == '+') {
		if (maps[me.r][me.c] == 'w') maps[me.r][me.c] = '.'; // 원래가 소문자면 점
		else if (maps[me.r][me.c] == 'W') maps[me.r][me.c] = '+'; // 대문자였으면 목표점

		if (maps[dy][dx] == '+') maps[dy][dx] = 'W';
		else  maps[dy][dx] = 'w';
	}
	else if (maps[dy][dx] == 'b' || maps[dy][dx] == 'B') {
		int ndy = dy + D[dir].r;
		int ndx = dx + D[dir].c;
		//만약 벽이면
		if (maps[ndy][ndx] == '#') return; // 그 앞도 벽이면
		else if (maps[ndy][ndx] == 'b' || maps[ndy][ndx] == 'B') return;//그 앞이 박스면
		//빈공간이나 비어있는 목표점이면
		else if (maps[ndy][ndx] == '.') { // 비어있는 공간이면
			maps[ndy][ndx] = 'b';

			if (maps[dy][dx] == 'B') maps[dy][dx] = 'W';
			else if (maps[dy][dx] == 'b') maps[dy][dx] = 'w';

			//원래 내가 있던 곳은 원래대로 바꾸고
			if (maps[me.r][me.c] == 'w') maps[me.r][me.c] = '.'; // 원래가 소문자면 점
			else if (maps[me.r][me.c] == 'W') maps[me.r][me.c] = '+'; // 대문자였으면 목표점

		}
		else if (maps[ndy][ndx] == '+') {
			maps[ndy][ndx] = 'B';

			if (maps[dy][dx] == 'B') maps[dy][dx] = 'W';
			else if (maps[dy][dx] == 'b') maps[dy][dx] = 'w';

			//원래 내가 있던 곳은 원래대로 바꾸고
			if (maps[me.r][me.c] == 'w') maps[me.r][me.c] = '.'; // 원래가 소문자면 점
			else if (maps[me.r][me.c] == 'W') maps[me.r][me.c] = '+'; // 대문자였으면 목표점

		}
	}
	me.r = dy;
	me.c = dx;
}
void print() {
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			cout << maps[r][c];
		}
		cout << '\n';
	}
}
int check() {
	for (int r = 1; r < R; r++) {
		for (int c = 1; c <= C; c++) {
			if (maps[r][c] == 'b') return 0;
		}
	}
	return 1;
}
int simulation() {
	//cout << "start" << '\n';
	//print();
	int ret = check();
	if (ret) return 1;
	for (int i = 0; i < orders.size(); i++) {
		move(orders[i]);
		int ret = check();
		if (ret) return 1;
		/*if (orders[i] == 0) {
			cout << i+1 << "번째 : 위"  << '\n';
		}
		else if (orders[i] == 1) {
			cout << i+1 << "번째 : 오른"  << '\n';
		}
		else if (orders[i] == 2) {
			cout << i+1 << "번째 : 아래" << '\n';
		}
		else{
			cout << i+1 << "번째 : 왼" << '\n';
		}*/
	}
	return 0;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int tc = 1;
	while (1) {
		init();
		int ret = input();
		if (!ret) return 0;
		ret = simulation();
		if (ret == 1) {
			cout << "Game " << tc << ": complete" << '\n';
		}
		else {
			cout << "Game " << tc << ": incomplete" << '\n';
		}
		print();
		tc++;
	}
	return 0;
}
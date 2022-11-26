#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX_C (8)
struct POS {
	int r, c;
};
char chess[MAX_C + 2][MAX_C + 2];
POS D[] = { {-1,0}, {-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1} };
string hor;
POS king, dol;
int N;
vector<int> order;
void input() {
	cin >> hor;
	king.r = 9 - (hor[1] - 48); 
	king.c = (hor[0] - 'A') + 1;
	chess[king.r][king.c] = 'K';

	cin >> hor;
	dol.r = 9 - (hor[1] - 48);
	dol.c = (hor[0] - 'A') + 1;
	cin >> N;
	chess[dol.r][dol.c] = 'd';

	for (int i = 0; i < N; i++) {
		string a; cin >> a;
		if (a == "T") {
			order.push_back(0);
		}
		else if (a == "RT") {
			order.push_back(1);
		}
		else if (a == "R") {
			order.push_back(2);
		}
		else if (a == "RB") {
			order.push_back(3);
		}
		else if (a == "B") {
			order.push_back(4);
		}
		else if (a == "LB") {
			order.push_back(5);
		}
		else if (a == "L") {
			order.push_back(6);
		}
		else if (a == "LT") {
			order.push_back(7);
		}
	}
}
void move(int idx) {
	int dy = king.r + D[idx].r;
	int dx = king.c + D[idx].c;
	if (dy < 1 || dx < 1 || dy>8 || dx>8) return;
	if (dy == dol.r && dx == dol.c) {
		int ddy = dol.r + D[idx].r;
		int ddx = dol.c + D[idx].c;
		if (ddy < 1 || ddx < 1 || ddy>8 || ddx>8) return;
		dol.r = ddy;
		dol.c = ddx;
	}
	king.r = dy;
	king.c = dx;
	return;
}
void print() {
	for (int r = 1; r <= 8; r++) {
		for (int c = 1; c <= 8; c++) {
			cout << chess[r][c];
		}
		cout << '\n';
	}
	cout << '\n';
}
void solve() {
	fill(&chess[0][0], &chess[8][9], '.');
	for (int i = 0; i < N; i++) {
		chess[king.r][king.c] = '.';
		chess[dol.r][dol.c] = '.';
		move(order[i]);
		chess[king.r][king.c] = 'K';
		chess[dol.r][dol.c] = 'd';
	}
	char a = king.c - 1 + 'A';
	cout << a << 9 - king.r<<'\n';
	a = dol.c - 1 + 'A';
	cout << a << 9 - dol.r << '\n';
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	input();
	solve();

	return 0;
}
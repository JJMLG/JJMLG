#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
struct POS {
	int r, c;
};
struct ST {
	int r, c, d;
};
char chess[8 + 1][8 + 1];
char maps[8 + 1][8 + 1];
queue<POS> q;
vector<POS>wall;
void input(){
	for (int r = 0; r < 8; r++) {
		for(int c=0; c < 8; c++){
			cin >> chess[r][c];
			maps[r][c] = chess[r][c];
			if (chess[r][c] == '#') wall.push_back({ r,c });
		}
	}
}
void wallmove() {
	vector<POS> newwall;
	for (int i = 0; i < wall.size(); i++) {
		int r = wall[i].r;
		int c = wall[i].c;
		maps[r][c] = '.';
		if (r + 1 < 8) {
			maps[r+1][c] = '#';
			newwall.push_back({ r + 1, c });
		}
	}
	wall.clear();
	wall.resize(newwall.size());
	copy(newwall.begin(), newwall.end(), wall.begin());

}
void print() {
	for (int r = 0; r < 8; r++) {
		for (int c = 0; c < 8; c++) {
			cout << maps[r][c] << " ";
		}
		cout << '\n';
	}
	cout << '\n';
}
int solve() {
	POS D[] = { {-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1} };
	q = {};
	vector<POS> path;
	path.push_back({ 7,0 });
	q.push({ 7,0 });
	maps[7][0] = 'M';
	while(1){
		if (q.empty()) break;
		while (!q.empty()) {
			POS data = q.front(); q.pop();
			for (int i = 0; i < 8; i++) {
				POS newdata = data;
				newdata.r += D[i].r;
				newdata.c += D[i].c;
				if (newdata.r < 0 || newdata.c < 0 || newdata.r>7 || newdata.c>7) continue;
				if (maps[newdata.r][newdata.c] == '#') continue;
				if (newdata.r == 0 && newdata.c == 7) return 1;
				maps[newdata.r][newdata.c] = 'M';
			}
		}
		wallmove();
		for (int r = 0; r < 8; r++) {
			for (int c = 0; c < 8; c++) {
				if (maps[r][c] == 'M') {
					q.push({ r, c });
				}
			}
		}
		print();
	}
	return 0;
}
int main(void) {
	freopen("movingmaze.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	cout <<solve() <<'\n';
	return 0;
}
#include <iostream>
#include <vector>
#include <queue>
#define MAX_HW (1000)
using namespace std;

struct POS {
	int r, c, times;
};
int H, W;
int maps[MAX_HW + 2][MAX_HW + 2];
queue<POS>q;
void input() {
	cin >> H >> W;
	for (int r = 0; r < H; r++) {
		for(int c=0; c<W;c++){
			char cc; cin >> cc;
			if (cc == '.') {
				maps[r][c] = 0;
				q.push({ r,c,0 });
			}
			else maps[r][c] = cc - '0';
		}
	}
}
int simulation() {
	static int dr[] = { -1,-1,0,1,1,1,0,-1 };
	static int dc[] = { 0,1,1,1,0,-1,-1,-1 };
	POS data;
	while (!q.empty()) {
		data = q.front(); q.pop();
		for (int i = 0; i < 8; i++) {
			POS newdata = data;
			newdata.r += dr[i];
			newdata.c += dc[i];
			if (newdata.r < 0 || newdata.c < 0 || newdata.r >= H || newdata.c >= W) continue;
			if (maps[newdata.r][newdata.c]) {
				maps[newdata.r][newdata.c] -= 1;
				if (maps[newdata.r][newdata.c] == 0) {
					newdata.times += 1;
					q.push(newdata);
				}
			}
		}
	}
	return data.times;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	input();
	cout << simulation() << '\n';
	return 0;
}
#define _CRT_SECURE_NO_WARNINGS
#if 1
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>

using namespace std;
#define MAX_WH (1000)
struct ST {
	int r, c, d;
};
struct POS {
	int r, c;
};
vector<ST> q;
vector<POS> fire;
int visit[MAX_WH + 2][MAX_WH + 2];
char maps[MAX_WH + 2][MAX_WH + 2];
int T;
int H, W, SR, SC;

void init() {
	q.clear();
	fire.clear();
}
void print() {
	for (int r = 1; r <= H; r++) {
		for (int c = 1; c <= W; c++) {
			cout << maps[r][c];
		}
		cout << '\n';
	}		cout << '\n';

}
void input() {
	cin >> W >> H;
	for (int r = 1; r <= H; r++) {
		for (int c = 1; c <= W; c++) {
			cin >> maps[r][c];
			if (maps[r][c] == '@') {
				SR = r;
				SC = c;
				q.push_back({ SR,SC,1 });
			}
			else if (maps[r][c] == '*') {
				fire.push_back({ r,c });
			}
		}
	}
}
int BFS() {
	/* 지도 밖으로 나가는데 1초 걸리는데 생각없이 0으로 해서 틀림 */
	if (SR == 1 || SC == 1 || SR == H || SC == W) return 1; 

	POS D[] = { {-1,0},{0,1},{1,0},{0,-1} };

	fill(&visit[0][0], &visit[MAX_WH + 1][MAX_WH + 2], 0);
	visit[SR][SC] = 1;
	vector<ST> newpath;
	vector<POS> newfire;
	while (1) {
		// 불붙이기
		newfire.clear();
		for (int i = 0; i < fire.size(); i++) {
			for (int idx = 0; idx < 4; idx++) {
				int dy = fire[i].r + D[idx].r;
				int dx = fire[i].c + D[idx].c;
				if (dy<1 || dx<1 || dy>H || dx>W) continue;
				if (maps[dy][dx] == '#') continue;
				if (maps[dy][dx] == '*') continue;
				maps[dy][dx] = '*';
				newfire.push_back({ dy,dx });
			}
		}
		fire.clear();
		fire.resize(newfire.size());
		copy(newfire.begin(), newfire.end(), fire.begin());

		//길가기
		// 만약에 newpath에 사이즈가 없으면 break;
		// 아니면 다시 채워넣고
		newpath.clear();
		if (q.empty()) break;
		for (int z = 0; z < q.size(); z++) {
			ST data = q[z];
			for (int i = 0; i < 4; i++) {
				ST newdata = data;
				newdata.r += D[i].r;
				newdata.c += D[i].c;
				newdata.d++;
				if (newdata.r<1 || newdata.c<1 || newdata.r>H || newdata.c>W) continue;
				if (maps[newdata.r][newdata.c] == '.' && (newdata.r == 1 || newdata.c == 1 || newdata.r == H || newdata.c == W)) {
					return newdata.d;
				}
				if (visit[newdata.r][newdata.c]) continue;
				if (maps[newdata.r][newdata.c] == '#') continue;
				if (maps[newdata.r][newdata.c] == '*') continue;
				newpath.push_back({ newdata.r, newdata.c, newdata.d });
				maps[newdata.r][newdata.c] = '@';
				visit[newdata.r][newdata.c] = 1;
			}
		}
		if (newpath.empty()) break;
		q.clear();
		q.resize(newpath.size());
		copy(newpath.begin(), newpath.end(), q.begin());
	}
	return -1;
}
void solve() {
	int ret = BFS();
	if (ret == -1) cout << "IMPOSSIBLE\n";
	else cout << ret << '\n';
}

int main(void) {
	freopen("fire.txt", "r", stdin);
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
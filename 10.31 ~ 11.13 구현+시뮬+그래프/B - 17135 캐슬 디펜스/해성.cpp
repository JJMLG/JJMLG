#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define MAX_NM (15)

struct EN {
	int r, c;
};
struct POS {
	int r, c, d;
};
map<int, EN> enermy;
int N, M, D;
int origin_maps[MAX_NM + 2][MAX_NM + 2];
int maps[MAX_NM + 2][MAX_NM + 2];

vector<int>comb_archer;

queue<POS> q;
int chk[MAX_NM + 2][MAX_NM + 2];
int result;

void input() {
	cin >> N >> M >> D;
	int idx = 1;
	for (int r = 1; r <= N; r++) {
		for (int c = 1; c <= M; c++) {
			cin >> origin_maps[r][c];
			if (origin_maps[r][c]) {
				if (enermy.find(idx) == enermy.end()) {
					enermy.insert({ idx,{r,c} });
					origin_maps[r][c] = idx;
					idx++;
				}
			}
		}
	}
}
bool COMP(POS a, POS b) {
	if (a.d == b.d) {
		return a.c < b.c;
	}
	return a.d < b.d;
}

POS findenermy(int sr, int sc) {
	static int dr[] = { 0,-1,0,1 };
	static int dc[] = { -1,0,1,0 };
	q = {};
	vector<POS> short_path;
	fill(&chk[0][0], &chk[MAX_NM + 1][MAX_NM + 2], 0);
	q.push({ sr,sc ,0 });
	chk[sr][sc] = 1;
	int shortest = D;
	while (!q.empty()) {
		POS data = q.front(); q.pop();
		if (data.d == shortest) {
			sort(short_path.begin(), short_path.end(), COMP);
			if (short_path.size()) {
				return short_path[0];
			}
			else return { 0,0,0 };
		}
		else {
			for (int i = 0; i < 4; i++) {
				POS newdata = data;
				newdata.r += dr[i];
				newdata.c += dc[i];
				newdata.d += 1;
				if (newdata.c<1 || newdata.r<1 || newdata.r>N || newdata.c>M) continue;
				if (chk[newdata.r][newdata.c]) continue;
				if (newdata.d > D) continue;
				q.push(newdata);
				chk[newdata.r][newdata.c] = 1;
				if (maps[newdata.r][newdata.c] && newdata.d <= shortest) {
					shortest = newdata.d;
					short_path.push_back(newdata);
				}
			}
		}
	}
	return { 0,0,0 };
}
void move_enermy() {

	for (int c = 1; c <= M; c++) {
		maps[N + 1][c] = 0;// 성으로 온 녀석들 제외처리
	}
	for (int c = 1; c <= M; c++) {
		for (int r = N; r >= 1; r--) {
			maps[r][c] = maps[r - 1][c];
		}
	}
}
int check() {
	for (int r = 1; r <= N; r++) {
		for (int c = 1; c <= M; c++) {
			if (maps[r][c]) return 1;
		}
	}
	return 0;
}
int defense() {
	int cnt = 0;
	copy(&origin_maps[0][0], &origin_maps[MAX_NM + 1][MAX_NM + 2], &maps[0][0]);// 맵원래대로 복사
	//궁수입력
	for (int i = 0; i < 3; i++) {
		int archeridx = comb_archer[i];
		maps[N + 1][archeridx] = archeridx;
	}
	while (check()) { // 적이 남아있는동안 계속
		vector<POS> erase_enermy; // 지워야할 적

		//궁수공격
		for (int i = 0; i < 3; i++) {
			POS en = findenermy(N + 1, comb_archer[i]);
			if (en.d != 0) {
				erase_enermy.push_back(en);
			}
		}

		//적지우기
		for (int i = 0; i < erase_enermy.size(); i++) {
			int r = erase_enermy[i].r;
			int c = erase_enermy[i].c;
			if (maps[r][c]) {
				maps[r][c] = 0;
				cnt++;
			}
		}
		// 이동하기
		move_enermy(); // 체크대신해도되겠다
	}
	return cnt;
}

void make_comb_archer(int start, int cnt) {
	if (cnt == 3) {
		int temp = defense();
		if (result < temp) result = temp;
		return;
	}
	for (int i = start; i <= M; i++) {
		if (comb_archer.size() && (i == comb_archer.back() || i < comb_archer.back())) {
			continue;
		}
		comb_archer.push_back(i);
		make_comb_archer(start + 1, cnt + 1);
		comb_archer.pop_back();
	}
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	input();
	make_comb_archer(1, 0);
	cout << result;
	return 0;
}

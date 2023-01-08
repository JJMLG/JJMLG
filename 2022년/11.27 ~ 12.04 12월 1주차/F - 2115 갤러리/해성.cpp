#define _CRT_SECURE_NO_WARNINGS

// 빈공간에서 상하좌우를 살펴봄
// 만약 위 벽에 그림을 걸경우 빈공간이 우쪽으로 연속해서 2번이상 향해야하고 위는 벽이여야함
// 개수를 센다음 어차피 그림 길이는 2니까 2로 나눔
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX_NM (1000)

struct POS {
	int r, c;
};
int R, C;
char maps[MAX_NM + 2][MAX_NM + 2];
int visit[4][MAX_NM + 2][MAX_NM + 2];
vector<POS> spaces;
int result[4];
int answer;
void input() {
	cin >> R >> C;
	fill(&visit[0][0][0] , &visit[3][MAX_NM + 1][MAX_NM + 2], 0);
	fill(&result[0], &result[3], 0);
	spaces.clear();
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			cin >> maps[r][c];
			if (maps[r][c] == '.') spaces.push_back({ r,c });
		}
	}
}
int check(int sr, int sc, int didx) {
	int cnt = 0;
	if(didx==0){//상
		for (int c = sc; c < C; c++) {
			if (maps[sr][c] != '.' || maps[sr-1][c]!='X') return cnt / 2;
			visit[didx][sr][c] = 1;
			cnt++;
		}
	}
	else if (didx == 1) {//하
		for (int c = sc; c < C; c++) {
			if (maps[sr][c] != '.' || maps[sr + 1][c] != 'X') return cnt / 2;
			visit[didx][sr][c] = 1;
			cnt++;
		}
	}
	else if (didx == 2) {//좌
		for (int r = sr; r < R; r++) {
			if (maps[r][sc] != '.' || maps[r][sc-1] != 'X') return cnt / 2;
			visit[didx][r][sc] = 1;
			cnt++;
		}
	}
	else if (didx == 3) {//우
		for (int r = sr; r < R; r++) {
			if (maps[r][sc] != '.' || maps[r][sc + 1] != 'X') return cnt / 2;
			visit[didx][r][sc] = 1;
			cnt++;
		}
	}

}
void solve() {
	//상 하 좌 우, 방향 순으로 연결되는지 체크하고 연결이 끝나면 2로 나눈 수를 해당 인덱스의 값에 넣어주자
	for (int i = 0; i < spaces.size(); i++) {
		for (int didx = 0; didx < 4; didx++) {
			if (visit[didx][spaces[i].r][spaces[i].c]) continue;
			int ret = check(spaces[i].r, spaces[i].c, didx);
			result[didx] += ret;
			answer += ret;
		}
	}
	cout << answer << '\n';
}
int main(void) {	
	freopen("2115_galery.txt","r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	solve();
	return 0;

}
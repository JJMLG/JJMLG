#include <iostream>
using namespace std;
#define MAX_NM (50)
struct RB {
	int r, c, dir;
}robot;
struct POS {
	int r, c;
};
POS D[] = { {-1,0},{0,1},{1,0},{0,-1} };
int revd[] = { 2,3,0,1 };
int N, M, result;
int maps[MAX_NM + 2][MAX_NM + 2];
void input() {
	cin >> N >> M;
	cin >> robot.r >> robot.c >> robot.dir;
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			cin >> maps[r][c];
		}
	}
}
int check() {
	for (int i = 1; i < 4; i++) { // 현재방향의 왼쪽부터 시작
		int newd = robot.dir - 1 * i;
		if (newd < 0) newd = (robot.dir + 4) - (1 * i);//방향 재정의
		int dy = robot.r + D[newd].r;
		int dx = robot.c + D[newd].c;
		if (!maps[dy][dx]) return 1;
	}
	return 0;
}
void print() {
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			cout << maps[r][c] << '\n';
		}
		cout << '\n';
	}cout << '\n';
}
int rotates() {
	for (int i = 1; i <= 4; i++) { // 현재방향의 왼쪽부터 시작
		int newd = robot.dir - 1 * i;
		if (newd < 0) newd = (robot.dir + 4) - (1 * i);//방향 재정의
		int dy = robot.r + D[newd].r;
		int dx = robot.c + D[newd].c;
		if (!maps[dy][dx]) {
			robot.dir = newd;
			robot.r = dy;
			robot.c = dx;
			return 1;
		}
	}
	return 0;
}
int simulation() {
	int result = 0;
	for (;;) {
		//1 현재위치 청소
		if (!maps[robot.r][robot.c]) {
			maps[robot.r][robot.c] = 2;
			result++;
		}
		
		int ret = rotates();
		if (!ret) {
			int opd = revd[robot.dir];
			int dy = robot.r + D[opd].r;
			int dx = robot.c + D[opd].c;
			if (maps[dy][dx]==1) {//만약 뒤쪽도 벽이면
				break; // 2-4 작동멈춘다
			}
			else { // 한칸 후진
				robot.r = dy;
				robot.c = dx;
				continue;
			}
		}
	}
	return result;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	input();
	cout << simulation() << '\n';
}
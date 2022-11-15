#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
#define MAX_NM (300)

int record[MAX_NM + 2][MAX_NM + 2];
int maps[MAX_NM + 2][MAX_NM + 2];
int IceGroup[MAX_NM + 2][MAX_NM + 2];
int N, M;
struct POS {
	int r, c;
};
queue<POS>q;
void input(){
	cin >> N >> M;
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			cin >> maps[r][c];
		}
	}
}
void count_record_Melt(int nr, int nc) {
	static int dr[] = { -1,0,1,0 };
	static int dc[] = { 0,1,0,-1 };
	int cnt = 0;
	for (int i = 0; i < 4; i++) {
		int dy = nr + dr[i];
		int dx = nc + dc[i];
		if (dy < 0 || dx < 0 || dy >= N || dx >= M) continue;
		if (!maps[dy][dx]) cnt++; // 주위 바닷물이면 바닷물 갯수 추가
	}
	record[nr][nc] = cnt;
}
int meltIce() {
	fill(&record[0][0], &record[MAX_NM + 1][MAX_NM + 2], 0);
	//바닷물 수 기록
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++){
			if (!maps[r][c])continue; // 해당위치 0이면
			count_record_Melt(r, c); // 주위 바닷물 수 세고 기록
		}
	}
	//바닷물 기록된만큼 제거
	int flag = 0;
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			if (!record[r][c]) continue;//전부다 띵굴수도
			if (!maps[r][c]) continue;
			maps[r][c] -= record[r][c];
			if (maps[r][c] < 0) maps[r][c] = 0;
			flag = 1;
		}
	}
	return flag;
}
void floodfill(int nr, int nc, int groupcnt) {
	static int dr[] = {-1,0,1,0};
	static int dc[] = {0,1,0,-1};
	q = {};
	q.push({ nr, nc });
	IceGroup[nr][nc] = groupcnt;
	while (!q.empty()) {
		POS data = q.front(); q.pop();
		for (int i = 0; i < 4; i++) {
			POS newdata = data;
			newdata.r += dr[i];
			newdata.c += dc[i];
			if (newdata.r < 0 || newdata.c < 0 || newdata.r >= N || newdata.c >= M) continue;
			if (!maps[newdata.r][newdata.c]) continue; // 빙산 없으면 패스
			if (IceGroup[newdata.r][newdata.c]) continue; //그룹다르면 패스
			IceGroup[newdata.r][newdata.c] = groupcnt;
			q.push(newdata);
		}
	}
}
int simulation(){
	for (int time = 1; ; time++) {
		int ret = meltIce(); //다녹을때까지 분리 안되면
		if (!ret) return 0; // 현재 빙산이 0이면
		//한덩어리빙산 주어진다니까 첨부터 답나오는건 신경 x

		// 빙산덩어리 수 확인
		int groupcnt = 0;

		fill(&IceGroup[0][0], &IceGroup[MAX_NM + 1][MAX_NM + 2], 0);
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				if (!maps[r][c]) continue;
				if (IceGroup[r][c]) continue;
				groupcnt++;
				if (groupcnt >= 2) return time;
				floodfill(r,c, groupcnt);
			}
		}
	}
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	input();
	cout << simulation() << '\n';
	return 0;
}
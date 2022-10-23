#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX_N (20)

struct POS 
{
	int r, c, d;
};
queue<POS> q;
vector<POS> path;

struct SHK 
{
	int r, c, size, eatcnt;
} babyshark;

int maps[MAX_N + 1][MAX_N + 1];
int visit[MAX_N + 1][MAX_N + 1];
int N;

void input() 
{
	cin >> N;
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			cin >> maps[r][c];
			if (maps[r][c] == 9) {
				babyshark.r = r;
				babyshark.c = c;
				babyshark.size = 2;
				babyshark.eatcnt = 0;
				maps[r][c] = 0;
			}
		}
	}
}
bool COMP(POS a, POS b) {
	if (a.d == b.d) {
		if (a.r == b.r) {
			return a.c < b.c;
		}
		else return a.r < b.r;
	} 
	return a.d < b.d;
}
int findfish() 
{
	static int dr[] = { -1,0,1,0 };
	static int dc[] = { 0,1,0,-1 };
	q = {};
	fill(&visit[0][0], &visit[MAX_N][MAX_N + 1], 0);
	q.push({ babyshark.r, babyshark.c, 0 });
	visit[babyshark.r][babyshark.c] = 1;
	int shortest = 0xf777777;
	while (!q.empty()) {
		POS data = q.front(); q.pop();
		if (data.d == shortest) {
			sort(path.begin(), path.end(), COMP);
			babyshark.r = path[0].r;
			babyshark.c = path[0].c;
			babyshark.eatcnt++;
			if (babyshark.eatcnt == babyshark.size) {
				babyshark.eatcnt = 0;
				babyshark.size++;
			}
			maps[babyshark.r][babyshark.c] = 0;
			return shortest;
		}
		for (int i = 0; i < 4; i++) {
			POS newdata = data;
			newdata.r += dr[i];
			newdata.c += dc[i];
			newdata.d += 1;
			if (newdata.r < 0 || newdata.c < 0 || newdata.r >= N || newdata.c >= N) continue;
			if (visit[newdata.r][newdata.c]) continue;
			if (maps[newdata.r][newdata.c] > babyshark.size) continue; // 물고기가 더 크다면 통과 못함
			visit[newdata.r][newdata.c] = 1;
			q.push(newdata);
			if (maps[newdata.r][newdata.c] && maps[newdata.r][newdata.c] < babyshark.size && shortest>= newdata.d) {
				path.push_back(newdata);
				shortest = newdata.d;
			}
		}
	}
	return -1;
}
int simulation() 
{
	int result = 0;
	for (;;) 
	{
		path.clear();
		int temp = findfish();
		if (temp == -1) return result;
		result += temp;
	}
}
int main(void) 
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);

	input();
	cout << simulation() << '\n';
	return 0;
}
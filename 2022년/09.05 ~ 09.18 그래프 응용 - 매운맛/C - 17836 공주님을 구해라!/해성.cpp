#include <iostream>
#include <queue>
using namespace std;
struct ST
{
	int cnt;
	bool sord;
	int r, c;
};
struct COMP
{
	bool operator()(const ST& a, const ST& b)
	{
		return	a.cnt > b.cnt;
	}
};
//세로, 가로 제한시간
int N, M, T;
int arr[100 + 1][100 + 1];
int check[100 + 1][100 + 1];
int visit[2][100 + 1][100 + 1];
priority_queue<ST, vector<ST>, COMP> pq;
void input()
{
	cin >> N >> M >> T;
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			cin >> arr[r][c];
		}
	}
}
void init()
{
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			check[r][c] = 0xf777777;
		}
	}
}
int BFS()
{
	static int dr[] = { -1,0,1,0 };
	static int dc[] = { 0,1,0,-1 };
	pq.push({ 0,false,0,0 });
	visit[0][0][0] = 1;
	while (!pq.empty())
	{
		ST DATA = pq.top(); pq.pop();
		if (DATA.cnt > T) continue;
		if (DATA.r == N - 1 && DATA.c == M - 1) return DATA.cnt;

		for (int i = 0; i < 4; i++) {
			ST newdata = DATA;
			newdata.r += dr[i];
			newdata.c += dc[i];
			newdata.cnt += 1;
			if (newdata.r<0 || newdata.c<0 || newdata.r>N - 1 || newdata.c>M - 1) continue;
			//벽일때, 1. 소드가 없으면 패스
			if (arr[newdata.r][newdata.c] == 1 && DATA.sord == false) continue;
			//있으면 방문처리
			if (arr[newdata.r][newdata.c] == 1 && DATA.sord == true)
			{
				if (visit[1][newdata.r][newdata.c]) continue;
				visit[1][newdata.r][newdata.c] = 1;
				check[newdata.r][newdata.c] = newdata.cnt;
				pq.push(newdata);
			}
			//벽아닐때 소드가 없으면
			if (arr[newdata.r][newdata.c] != 1)
			{
				//소드가 있는 곳이면
				if (arr[newdata.r][newdata.c] == 2)
				{
					newdata.sord = true;
					if (visit[1][newdata.r][newdata.c]) continue;
					check[newdata.r][newdata.c] = newdata.cnt;
					visit[1][newdata.r][newdata.c] = 1;
					pq.push(newdata);
				}
				// 없는 곳이면
				else
				{
					//소드가 있으면
					if (DATA.sord)
					{
						if (visit[1][newdata.r][newdata.c]) continue;
						check[newdata.r][newdata.c] = newdata.cnt;
						visit[1][newdata.r][newdata.c] = 1;
						pq.push(newdata);
					}
					//없으면
					else {
						if (visit[0][newdata.r][newdata.c]) continue;
						check[newdata.r][newdata.c] = newdata.cnt;
						visit[0][newdata.r][newdata.c] = 1;
						pq.push(newdata);
					}
				}
			}
		}
	}
	return -1;
}
int main(void)
{
	input();
	init();
	int ans = BFS();
	if (ans == -1) cout << "Fail" << '\n';
	else cout << ans << '\n';
	return 0;
}

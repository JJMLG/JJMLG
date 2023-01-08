#include <iostream>
#include <set>
#include <queue>
using namespace std;
int N, M, K;
//set<int> s;
int maxidx = 0;
int minidx = 0xf777777;
struct ST
{
	int r, c;
};
queue<ST> q;
int maxx = 0;
int arr[1000 + 3][1000 + 3];
int visit[1000 + 3][1000 + 3];
void input() 
{
	cin >> N >> M >> K;
	for (int r = 1; r <= N; r++) {
		for (int c = 1; c <= M; c++) {
			cin >> arr[r][c];
			if (maxidx < arr[r][c]) maxidx = arr[r][c];
			if (minidx > arr[r][c]) minidx = arr[r][c];

		}
	}
}
void init() 
{
	for (int r = 0; r <= N + 1; r++)
	{
		for (int c = 0; c <= M + 1; c++)
		{
			if (r == N + 1) arr[r][c] = -1;
			else if ((r == 0) || (c == 0 || c == M + 1)) arr[r][c] = 0;
			visit[r][c] = arr[r][c];
		}
	}
}
static int dr[] = { -1,0,1,0 };
static int dc[] = { 0,1,0,-1 };
int check(int r, int c) 
{
	for (int i = 0; i < 4; i++) 
	{
		int dy = r + dr[i];
		int dx = c + dc[i];
		if (dy<0 || dx<0 || dy>N+1 || dx>M+1) continue;
		if (!visit[dy][dx]) return 1;
	}
	return 0;
}
int BFS(int possible) 
{
	int sum = 0;
	init();
	q = {};
	for (int r = 1; r <= N; r++) 
	{
		for (int c = 1; c <= M; c++) 
		{
			if (r == 1) 
			{
				if (visit[r][c] > possible) continue;
				q.push({ r,c });
				visit[r][c] = 0;
				sum++;
			}
			else if (c == 1 || c == M) 
			{
				if (!visit[r][c]) continue;
				if (visit[r][c] > possible) continue;
				q.push({ r,c });
				visit[r][c] = 0;
				sum++;
			}
		}
	}
	while (!q.empty()) 
	{
		ST DATA = q.front(); q.pop();
		for (int i = 0; i < 4; i++) 
		{
			ST newdata = DATA;
			newdata.r += dr[i];
			newdata.c += dc[i];
			//경계밖이면 패스
			if (newdata.r<1 || newdata.c<1 || newdata.r>N || newdata.c>M) continue;
			//가능한 채굴 강도보다 크다면 패스
			if (arr[newdata.r][newdata.c] > possible) continue;
			//이미 채굴했으면 패스
			if (!visit[newdata.r][newdata.c]) continue;
			// 주변에 공기가 없으면 패스
			if (!check(newdata.r, newdata.c)) continue;
			visit[newdata.r][newdata.c] = 0;
			q.push(newdata);
			sum++;
			if (sum >= K) return 1;
		}
	}
	return 0;
}
int solve()
{
	int ans=0;
	int mid=maxidx;
	while (minidx<=maxidx) 
	{
		mid = (minidx + maxidx) / 2;
		if (BFS(mid)) 
		{
			ans = mid;
			maxidx = mid - 1;
		}
		else 
		{
			minidx = mid + 1;
		}
	}
	return ans;
}
int main(void) 
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	input();
	int ans = solve();
	cout << ans;
	return 0;
}

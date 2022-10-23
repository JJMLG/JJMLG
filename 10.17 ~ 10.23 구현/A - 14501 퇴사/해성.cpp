#include <iostream>
#include <vector>
using namespace  std;
int N, maxx;
vector<int> days;
vector<int> costs;
void input() 
{
	cin >> N;
	days.push_back(0);
	costs.push_back(0);
	for (int i = 1; i <= N; i++) {
		int d, cost; cin >> d >> cost;
		days.push_back(d);
		costs.push_back(cost);
	}
}
void DFS(int nowday, int costsum)
{
	if (nowday > N) {
		if (maxx < costsum) maxx = costsum;
		return;
	}
	DFS(nowday + 1, costsum);
	if (nowday + days[nowday] <= N+1) DFS(nowday + days[nowday], costsum + costs[nowday]);
//
//=	for (int i = nowday; i <= N; i++) {
//	int newday = nowday + days[i];
//	if (newday > N) continue;
//	int newcost = costsum + costs[nowday];
//	DFS(newday, newcost);
//	}
}
void solve() 
{
	//for (int i = 1; i <= N; i++) {
	//	if (days[i] + i-1 > N) continue;
	DFS(1, 0);
	//}
}
int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	input();
	solve();
	cout << maxx << '\n';
	return 0;
}
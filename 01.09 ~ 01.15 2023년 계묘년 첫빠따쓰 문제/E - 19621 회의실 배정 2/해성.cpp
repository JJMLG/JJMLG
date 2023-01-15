#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int N;
struct MT{
	int start, end, cnt;
};
vector<MT> meet;
int dp[26];
int main(void) {
	cin >> N;
	int maxx = 0;
	for (int i = 0; i < N; i++) {
		int s, e, c; cin >> s >> e >> c;
		meet.push_back({ s,e,c });
	}
	for (int i = 0; i < N; i++) {
		if (i < 2) {
			dp[i] = meet[i].cnt;
		}
		else {
			dp[i] = meet[i].cnt + *max_element(dp, dp + i - 1);
		}
	}

	cout << *max_element(dp, dp+N);
	return 0;
}
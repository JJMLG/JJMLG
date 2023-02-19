// 다시 풀어야 할 문제
#include <iostream>
#include <vector>

using namespace std;

#define MAX_T (10000)
struct CO {
	int coin, cnt;
};
vector<CO>coins;
vector<int> arr;
int dp[10000 + 1];
int T, K;
void input() {
	cin >> T >> K;
	for (int i = 0; i < K; i++) {
		int pi, ni; cin >> pi >> ni;
		coins.push_back({ pi, ni });
	}	
}
void solve() {
	dp[0] = 1;
	for (int i = 0; i < K; i++) {
		for (int total = T; total >= 0; total--) {
			for (int c = 1; c <= coins[i].cnt; c++) {
				if (total - coins[i].coin * c >= 0)	dp[total] += dp[total - coins[i].coin * c];
			}
		}
	}
	cout << dp[T]<<'\n';
}
int main(void) {
	input();
	solve();
	return 0;
}

// DFS 시간초과
//#include <iostream>
//#include <vector>
//#include<algorithm>
//
//using namespace std;
//
//#define MAX_K (100)
//
//struct CO {
//	int coin, cnt;
//};
//vector<CO>coins;
//int visit[MAX_K + 1];
//int T, K;
//void input() {
//	cin >> T >> K;
//	for (int i = 0; i < K; i++) {
//		int pi, ni; cin >> pi >> ni;
//		coins.push_back({ pi, ni });
//	}	
//}
//int result = 0;
//void DFS(int dep, int val) {
//	if (val > T) return;
//	if (dep >= K) {
//		/*for (int i = 0; i < K;i++) {
//			cout << coins[i].coin << " " << visit[i] << '\n';
//		}
//		cout << "===============================\n";*/
//		if (val == T) {
//			result++;
//		}
//		return;
//	}
//	for (int i = 0; i <= coins[dep].cnt; i++) {
//		//visit[dep] = i;
//		DFS(dep+1, val + coins[dep].coin * i);
//		//visit[dep] = 0;
//	}
//}
//void solve() {
//	DFS(0, 0);
//	cout << result;
//}
//int main(void) {
//	input();
//	solve();
//	return 0;
//}

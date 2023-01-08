#define _CRT_SECURE_NO_WARNINGS
#if 1
#include<iostream>
#include<algorithm>

using namespace std;
#define MAX_N (1000)
int N;
int dp[MAX_N + 1];
int card[MAX_N + 1];
void input() {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> card[i];
	}
}
void solve() {
	dp[1] = card[1];
	for (int i = 2; i <= N; i++) {
		for (int j = 0; j < i; j++) {
			dp[i] = max(dp[i], card[i - j] + dp[j]);
		}
	}
	cout << dp[N];
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	solve();
	return 0;
}

#endif

#if 0
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N;
int cards[10000 + 1];
int dp[10000 + 1];

int main(void) {
	freopen("11052card.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	for (int i = 1; i <= N; i++) {
		cin >> cards[i];
	}
	dp[0] = 0;
	dp[1] = cards[1];
	for (int i = 2; i <= N; i++) {
		for (int j = 0; j < i; j++) {
			dp[i] = max(dp[i], dp[j] + cards[i - j]);
		}
	}
	cout << dp[N];

	return 0;
}
#endif
#if 0
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N;
int cards[10000 + 1];
int comb[10000 + 1];
int maxx = 0;
void DFS(int dep, int left) {
	if (left < 0) return;
	if (dep > N) {
		if (left == 0) {
			int cnt = 0;
			for (int i = 1; i <= dep; i++) {
				//cout << comb[i] << " ";
				cnt += (comb[i] * cards[i]);
			}
			//cout << '\n';
			if (cnt > maxx) maxx = cnt;
		}
			return;
	}
	for (int i = 0; i <= left / dep; i++) {
		comb[dep] = i;
		DFS(dep + 1, left - (i * dep));
	}
}
void solve() {
	DFS(1, N);
	cout << maxx;
}
int main(void) {
	freopen("11052card.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	for (int i = 1; i <= N; i++ ) {
		cin >> cards[i];
	}

	solve();

	return 0;
}
#endif
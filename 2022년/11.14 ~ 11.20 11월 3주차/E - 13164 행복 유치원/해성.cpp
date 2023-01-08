#define _CRT_SECURE_NO_WARNINGS
#if 1
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define MAXN (300000)
int N, K;
long long maxx;
int student[MAXN + 1];
vector<int>perms;
vector<int> diffs;
void input() {
	cin >> N >> K;
	for (int i = 1; i <= N; i++) {
		cin >> student[i];
	}
}
long long solve() {
	for (int i = 1; i < N; i++) {
		diffs.push_back(student[i + 1] - student[i]);
	}
	sort(diffs.begin(), diffs.end());
	long long result = 0;
	for (int i = 0; i < N - K; i++) {
		result += diffs[i];
	}
	return result;
}
int main(void) {
	freopen("13164.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	cout << solve() << '\n';
	return 0;

}
#endif
#if 0
//#include <iostream>
//#include <vector>
//#include <algorithm>
//
//using namespace std;
//#define MAXN (300000)
//int N, K;
//long long maxx;
//int student[MAXN + 1];
//vector<int>perms;
//
//void input() {
//	cin >> N >> K;
//	for (int i = 1; i <= N; i++) {
//		cin >> student[i];
//	}
//}
//long long calc() {
//	long long start = 1;
//	long long end;
//	long long sums = 0;
//	for (int i = 0; i < perms.size(); i++) {
//		if (perms[i] == 1) {
//			start ++;
//		}
//		else {
//			end = start + perms[i]-1;
//			sums += (student[end] - student[start]);
//			start = end + 1;
//		}
//	}
//	return sums;
//}
//void DFS(int dep, int cnt) {
//	if (dep == K - 1) {
//		if (cnt == 0) return;
//		perms.push_back(cnt);
//		//for (int i = 0; i < perms.size(); i++) {
//		//	cout << perms[i] << " ";
//		//}
//		//cout << '\n';
//		long long ret = calc();
/////		cout << ret << '\n';
//		if (maxx > ret) maxx = ret;
//		perms.pop_back();
//		return;
//	}
//	for (int i = 1; i <= cnt; i++) {
//		perms.push_back(i);
//		DFS(dep + 1, cnt-i);
//		perms.pop_back();
//	}
//}
//void solve() {
//	maxx = 0xf7777777;
//	DFS(0, N);
//	cout << maxx;
//}
//int main(void) {
//	freopen("13164.txt", "r", stdin);
//	ios_base::sync_with_stdio(false);
//	cin.tie(nullptr);
//	cout.tie(nullptr);
//	input();
//	solve();
//	return 0;
//
//}
#endif
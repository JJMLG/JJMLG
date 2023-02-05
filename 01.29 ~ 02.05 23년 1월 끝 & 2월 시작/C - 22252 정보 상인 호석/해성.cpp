#include <iostream>
#include <queue>
#include <unordered_map>
using namespace std;
unordered_map<string, priority_queue<int>> gorila;
int Q;

long long solve() {
	long long result = 0;
	cin >> Q;
	for (int i = 0; i < Q; i++) {
		int q; cin >> q;
		string name; cin >> name;
		if (q == 1) {
			int k; cin >> k;
			while (k--) {
				int C; cin >> C;
				gorila[name].push(C);
			}
		}
		else {
			int b; cin >> b;
			while (b-- && !gorila[name].empty()) {
				result += gorila[name].top();
				gorila[name].pop();
			}
		}
	}
	return result;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cout << solve() << '\n';
	return 0;
}
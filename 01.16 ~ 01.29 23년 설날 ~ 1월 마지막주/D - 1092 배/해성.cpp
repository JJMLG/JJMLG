#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, M;
vector<int> cranes;
vector<int> boxes;
void input() {
	cin >> N;
	cranes.resize(N);
	for (int i = 0; i < N; i++) {
		cin >> cranes[i];
	}
	cin >> M;
	boxes.resize(M);
	for (int i = 0; i < M; i++) {
		cin >> boxes[i];
	}
}
int solve() {
	sort(cranes.begin(), cranes.end(), greater<int>());
	sort(boxes.begin(), boxes.end(), greater<int>());
	int rep = 0;
	while (1) {
		rep++;
		for (int i = 0; i < N; i++) {
			for (int c = 0; c< M; c++) {
				if (boxes.size() <= c) break;
				if (cranes[i] >= boxes[c]) {
					boxes.erase(boxes.begin() + c);
					break;
				}
				if (i == 0 && cranes[0] < boxes[c]) return 0;
			}
			if (boxes.empty()) return rep;
		}
	}
	return rep;
}
int main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	input();
	int ret = solve();
	if (ret) cout << ret << '\n';
	else cout << -1 << '\n';
	return 0;
}
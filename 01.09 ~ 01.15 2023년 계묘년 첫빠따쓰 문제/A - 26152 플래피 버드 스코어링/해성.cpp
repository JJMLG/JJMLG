#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> arr;
vector<int>birds;
int N, Q;

void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int h; cin >> h;
		arr.push_back(h);
	}
	for (int i = 0; i < N; i++) {
		int h; cin >> h;
		arr[i] -= h;
		if (i > 0) {
			if (arr[i - 1] < arr[i]) arr[i] = arr[i - 1];
		}
	}

	cin >> Q;
	birds.resize(Q+1);
	for (int i = 0; i < Q; i++) {
		cin >> birds[i];
	}
}
int bs(int birdH) {
	int start = 0;
	int end = N-1;
	int rangeidx = -1;
	while (start <= end) {
		int mid = (start + end) / 2;
		if (arr[mid] >= birdH) {
			if (rangeidx < mid) rangeidx = mid;
			start = mid + 1;
		}
		else {
			end = mid - 1;
		}
	}
	return rangeidx;
}
void solve() {
	for (int i = 0; i < Q; i++) {
		int ret = bs(birds[i]);
		//cout << ret << "\n";
		if (ret == -1) cout << 0 << '\n';
		else cout << ret+1 << '\n';
	}
}
int main(void) {
	ios_base::sync_with_stdio(0); cin.tie(0);
	input();
	solve();
	return 0;
}

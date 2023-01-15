#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct INFO{
	int idx, h;
	
};
vector<INFO> arr;
vector<int>birds;
int N, Q;

bool COMP(INFO b, INFO a) {
	return a.h > b.h;
}
void input() {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		int h; cin >> h;
		arr.push_back({ i, h });
	}
	for (int i = 1; i <= N; i++) {
		int h; cin >> h;
		arr[i - 1].h -= h;
	}

	sort(arr.begin(), arr.end(), COMP);

	cin >> Q;
	birds.resize(Q);
	for (int i = 0; i < Q; i++) {
		cin >> birds[i];
	}
}
int bs(int bidx) {
	int start = 0;
	int end = N;
	int rangeidx = 2000000001;
	while (start <= end) {
		int mid = (start + end) / 2;
		if (arr[mid].h < bidx) {
			if (rangeidx > mid) rangeidx = mid;
			start = mid + 1;
		}
		else {
			end = mid - 1;
		}
	}
	return rangeidx;
}
bool comp(INFO a, INFO b) {
	return a.idx < b.idx;
}
void solve() {
	for (int i = 0; i < Q; i++) {
		int ret = bs(birds[i]);
		cout << ret << '\n';
		/*if (ret == -1) cout<< N << '\n';
		else {
			auto mins = min_element(arr.begin(), arr.begin() + ret+1, comp);
		//	cout << mins->idx-1 << "\n";*/
		//}
	}
}
int main(void) {
	ios_base::sync_with_stdio(0); cin.tie(0);
	input();
	solve();
	return 0;
}

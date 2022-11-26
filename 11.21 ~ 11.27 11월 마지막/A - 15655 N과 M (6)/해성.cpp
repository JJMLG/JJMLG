#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int N, M;
vector<int> arr;
vector<int> comb;
set<vector<int> > s;
void input() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		int num; cin >> num;
		arr.push_back(num);
	}
	sort(arr.begin(), arr.end());
}
void DFS(int start, int dep) {
	if (dep == M) {
		s.insert(comb);
	}
	for (int i = start; i < N; i++) {
		comb.push_back(arr[i]);
		DFS(i + 1, dep + 1);
		comb.pop_back();
	}
}
void print() {
	auto it = s.begin();
	while (it != s.end()) {
		for (int a : *it) cout << a << " ";
		cout << '\n';
		it++;
	}
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	DFS(0, 0);
	print();
	return 0;
}
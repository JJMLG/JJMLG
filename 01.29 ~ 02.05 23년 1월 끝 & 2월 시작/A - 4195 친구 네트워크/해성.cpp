#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <unordered_map>

using namespace std;

unordered_map<string, int> friendsNum;
vector<int> parent, nums;

void init() {
	friendsNum.clear();
	parent.clear();
	nums.clear();
}
int findParent(int num) {
	if (parent[num] == num) return num;
	return  parent[num] = findParent(parent[num]);
}
void uniteParent (int a, int b){
	a = findParent(a);
	b = findParent(b);
	
	if (a == b) return;

	if (a < b) {
		parent[b] = a;
		nums[a] += nums[b];
	}
	else if (a > b) {
		parent[a] = b;
		nums[b] += nums[a];
	}

}
void solve() {
	int F; cin >> F;
	parent.assign(F * 2 + 1, 0);
	nums.assign(F * 2 + 1, 1);

	for (int i = 0; i <= F*2; i++) {
		parent[i] = i;
	}

	int groupN=0, people1 = 0, people2 = 0;
	for (int i = 0; i < F; i++) {
		string A, B; cin >> A >> B;
		if (friendsNum.count(A) == 0) {
			friendsNum[A] = ++groupN;
			people1 = groupN;
		}
		else {
			people1 = friendsNum[A];
		}
		if (friendsNum.count(B) == 0) {
			friendsNum[B] = ++groupN;
			people2 = groupN;
		}
		else {
			people2 = friendsNum[B];
		}
		uniteParent(people1, people2);
		int target = findParent(people1);
		cout << nums[target] << '\n';
	}
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int T; cin >> T;
	for (int tc = 0; tc < T; tc++) {
		init();
		solve();
	}
	return 0;
}


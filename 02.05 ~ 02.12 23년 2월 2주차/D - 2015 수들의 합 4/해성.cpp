#include <iostream>
#include <vector>
#include <map>
using namespace std;
vector<int> sumTable;
int N;
int K;
map<int, long long> maps;
void input() {
	cin >> N >> K;
	for(int i = 0; i< N; i++){
		int n; cin >> n;
		if (i > 0) {
			sumTable.push_back(sumTable[i - 1] + n);
		}
		else {
			sumTable.push_back(n);
		}
	}
}
void solve() {
	int result = 0;
	for (int i = 0; i < N; i++) {
		if (sumTable[i] == K) result++;
		result+= maps[sumTable[i] - K];
		maps[sumTable[i]]++;
	}
	cout << result;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	solve();
	return 0;
}
#include <iostream>
#include <vector>

using namespace std;
#define MAX_N (250000)
int N, X;
vector<int> v;
void input() {
	cin >> N >> X;
	for (int i = 0; i < N; i++) {
		int n; cin >> n;
		v.push_back(n);
	}
}
void solve() {
	long long sum = 0;
	long long maxx;
	int cnt = 1;
	for (int i = 0; i < X; i++) {
		sum += v[i];
	}
	maxx = sum;
	for (int i = X; i < N; i++) {
		sum -= v[i-X];
		sum += v[i];
		if (sum > maxx) {
			maxx = sum;
			cnt = 1;
		}
		else if (sum == maxx) {
			cnt++;
		}
	}
	if (maxx == 0) cout << "SAD";
	else cout << maxx << '\n' << cnt;
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	solve();
	return 0;
}
#if 1
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int N;
struct OK {
	int idx, num;
};
vector<int> arr;
stack<OK> ST;
void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int n; cin >> n;
		arr.push_back(n);
	}
}
void solve() {
	for (int i = 0; i < N; i++) {
		if (i == 0) {
			ST.push({ i,arr[i] });
		}
		else {
			if (!ST.empty()) {
				while (!ST.empty() && ST.top().num < arr[i]) {
					arr[ST.top().idx] = arr[i];
					ST.pop();
				}
			}
			ST.push({ i, arr[i] });
		}
	}
	while (!ST.empty()) {
		arr[ST.top().idx] = -1;
		ST.pop();
	}
	for (int a : arr) cout << a << " ";
}
int main(void) {
	input();
	solve();
	return 0;
}
#endif

#if 0
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> pbs;
stack<int> st;
int N;
void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int a; cin >> a;
		pbs.push_back(a);
	}
}
void solve() {
	for (int i = 0; i < N; i++) {
		st.push(pbs[i]);
		int idx = i + 1;
		if (st.top() <= pbs[i]) {
			st.pop();
			while (1) {
				if (idx >= N) {
					pbs[i] = -1;
					break;
				}
				else if (pbs[idx] > pbs[i]) {
					st.push(pbs[idx]);
					pbs[i] = st.top();
					break;
				}
				idx++;
			}
		}
		else {
			pbs[i] = st.top();
		}
	}
	for (int i = 0; i < N; i++) {
		cout << pbs[i] << " ";
	}
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	input();
	solve();
	return 0;
}
#endif
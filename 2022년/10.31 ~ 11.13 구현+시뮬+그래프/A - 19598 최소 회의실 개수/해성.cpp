#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
int N;
struct MT {
	int s, e;
};
priority_queue<int, vector<int>, greater<int>> pq;
vector<MT> meet;
void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int s, e; cin >> s >> e;
		meet.push_back({ s,e });
	}
}
bool COMP(MT a, MT b) {
	return a.s < b.s;
}
int solve(){
	sort(meet.begin(), meet.end(), COMP);
	pq.push(meet[0].e);
	for (int i = 1; i < meet.size(); i++) {
		if (pq.top() <= meet[i].s) {
			pq.pop(); 
		}
		pq.push(meet[i].e);
	}
	return pq.size();
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	cout << solve() << '\n';
	return 0;
}
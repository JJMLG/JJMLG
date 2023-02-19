#include <iostream>
#include <queue>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

string words;

void input() {
	cin >> words;
}
long long check(long long s, long long len) {
	string temp = words.substr(s,len);
	string rev_temp = temp;
	reverse(rev_temp.begin(), rev_temp.end());
	if (temp == rev_temp) return 0;
	return len;
}
long long solve() {
	string temp = words;
	set<char> S;
	S.insert(words.begin(), words.end());
	if (S.size() == 1) return -1;
	for (long long i = words.size(); i >= 2; i--) {
		for (long long c = 0; c <= words.size() - i; c++) {
			long long ret = check(c, i);
			if (ret) {
				return i;
			}
		}
	}
	return -1;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	input();
	long long ret = solve();
	cout << ret;
	return 0;
}

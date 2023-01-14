#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
vector<int> arr;
vector<int> primes;
int N;
void input() {
	cin >> N;
	arr.resize(N + 1);
	fill(arr.begin(), arr.end(), 0);
}
void makePrime() {
	arr[0] = arr[1] = 1;
	for (int i = 2; i < (int)sqrt(N) + 1; i++) {
		if (arr[i]) continue;
		for (int j = i * 2; j <= N; j += i) {
			arr[j] = 1;
		}
	}
	for (int i = 2; i <= N; i++) {
		if (!arr[i]) {
			primes.push_back(i);
		}
	}
}
int solve() {
	int start, end, sum, cnt;
	start = end = cnt = 0;
	sum = primes[start];
	while (start < primes.size() && end < primes.size()) {
		if (sum == N) cnt++;
		if (sum < N) {
			end++;
			if (end == primes.size())break;
			sum += primes[end];
		}
		else if (sum >= N) {
			sum -= primes[start];
			start++;
		}
	}
	return cnt;
}
int main(void) {
	freopen("1644.txt", "r",stdin);
	input();
	makePrime();
	if (N == 1) cout << 0<<'\n';
	else cout << solve() <<'\n';

	return 0;
}
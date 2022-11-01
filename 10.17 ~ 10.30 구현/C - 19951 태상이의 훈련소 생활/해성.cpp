#include <iostream>
using namespace std;
#define MAX_N (100000)
int ground[MAX_N + 1];
int arr[MAX_N+ 1];
int N, M;
void input(void)
{
	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		cin >> ground[i];
	}
}
void simulation()
{
	for (int i = 0; i < M; i++) {
		int a, b, k; cin >> a >> b >> k;
		arr[a] += k;
		arr[b + 1] -= k;
	}
	for (int i = 1; i <= N; i++) {
		arr[i] += arr[i - 1];
	}
	for (int i = 1; i <= N; i++) {
		ground[i] += arr[i];
		cout << ground[i] << " ";
	}
}

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	input();

	simulation();
	return 0;
}
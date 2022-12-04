#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define LEN (10)
#define MAX_L (100)
int N, SR, SC, ER, EC;
int maps[MAX_L + 1][MAX_L + 1];
struct SQ {
	int sr, sc, er, ec;
};
vector<SQ> squares;
void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int c, r; cin >> c >> r;
		squares.push_back({ r, c, r + 10, c + 10 });
	}
	SR = squares[0].sr;
	SC = squares[0].sc;
	ER = squares[0].er;
	EC = squares[0].ec;
	for (int i = 0; i < squares.size(); i++) {
		SR = min(SR, squares[i].sr);
		ER = max(ER, squares[i].er);
		SC = min(SC, squares[i].sc);
		EC = max(EC, squares[i].ec);
	}
}
void makesqaure() {
	for (int i = 0; i < squares.size(); i++) {
		for (int r = squares[i].sr; r < squares[i].er; r++) {
			for (int c = squares[i].sc; c < squares[i].ec; c++) {
				maps[r][c] += 1;
			}
		}
	}
}
void print(int sr, int sc, int sizer, int sizec) {

	for (int r = 0; r < 100; r++) {
		for (int c = 0; c < 100; c++) {
			cout << maps[r][c];
		}
		cout << '\n';
	}
}
int check(int sr, int sc, int sizer, int sizec) {
	int cnt = 0;
	for (int r = sr; r < sr + sizer; r++) {
		for (int c = sc; c < sc + sizec; c++) {
			if (!maps[r][c]) return 0;
			cnt++;
		}
	}
	return cnt;
}
int	findMAX() {
	int maxx = 0;
	for (int sizeR = ER - SR; sizeR >= 1; sizeR--) {
		for (int sizeC = EC - SC; sizeC >= 1; sizeC--) {
			for (int sr = SR; sr <= ER - sizeR; sr++) {
				for (int sc = SC; sc <= EC - sizeC; sc++) {
					int ret = check(sr, sc, sizeR, sizeC);
					if (ret > maxx) {
						maxx = ret;
					}
				}
			}
		}
	}
	return maxx;
}
void solve() {
	makesqaure();
	cout << findMAX() << '\n';
}
int main(void) {
	freopen("2571_paper.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	solve();
	return 0;
}
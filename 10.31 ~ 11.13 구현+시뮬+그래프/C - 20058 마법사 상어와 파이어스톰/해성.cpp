#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cmath>
using namespace std;
#define MAX_N (64)
int arr[MAX_N + 2][MAX_N + 2];
int newarr[MAX_N + 2][MAX_N + 2];
int ffVisit[MAX_N + 2][MAX_N + 2];
int maxgroup;
int sumIce;
int N, Q;
int totalN;
vector<int> order;
struct POS {
	int r, c;
};
queue<POS> q;
void input(){
	cin >> N >> Q;
	totalN = pow(2, N);
	for (int r = 1; r <= totalN; r++) {
		for (int c = 1; c <= totalN; c++) {
			cin >> arr[r][c];
		}
	}
	for (int i = 0; i < Q; i++) {
		int cc; cin >> cc;
		order.push_back(cc);
	}
}
void print() {
	for (int r = 1; r <= totalN; r++) {
		for (int c = 1; c <= totalN; c++) {
			cout << arr[r][c] << " ";
		}
		cout << '\n';
	}
	cout << '\n';
}
void rotateGrid(int sr, int sc, int er, int ec, int lens) {
	for (int r = 0; r < lens; r++) {
		for (int c = 0; c < lens; c++) {
			newarr[sr + c][sc + lens - r - 1] = arr[sr + r][sc + c];
		}
	}
}
void rotate(int oidx) {
	int lens = pow(2, order[oidx]);
	int rep = totalN / lens;
	for (int r = 0; r < rep; r++) {
		for (int c = 0; c < rep; c++) {
			int sr = 1 + lens * r;
			int sc = 1 + lens * c;
			//cout << "sr : " << sr << "  sc : " << sc;
			//cout << '\n';
			int er = sr + lens - 1;
			int ec = sc + lens - 1;
			rotateGrid(sr, sc, er, ec, lens);
		}
	}
	//다 돌리고 나면 카피
	copy(&newarr[0][0], &newarr[MAX_N + 1][MAX_N + 2], &arr[0][0]);
}
int checkice(int sr, int sc) {
	static int dr[] = { -1,0,1,0 };
	static int dc[] = { 0,1,0,-1 };
	int cnt = 0;
	for (int i = 0; i < 4; i++) {
		int dy = sr + dr[i];
		int dx = sc + dc[i];
		if (dy<1 || dx<1 || dy>totalN || dx>totalN) continue;
		if (arr[dy][dx]) cnt++;
	}
	if (cnt < 3) return 0;
	return 1;
}
void firestorm() {
	for (int r = 1; r <= totalN; r++) {
		for (int c = 1; c <= totalN; c++) {
			int ret = checkice(r,c);
			if (!ret) newarr[r][c] = 1; //줄어야할 녀석
			else newarr[r][c] = 0; // 그대로
		}
	}
	for (int r = 1; r <= totalN; r++) {
		for (int c = 1; c <= totalN; c++) {
			// 빼야할 얼음이고 아직 얼음이 남아있는 경우만 빼기
			if (newarr[r][c] && arr[r][c]) arr[r][c] -= 1; 
		}
	}
}
int calcIceSum() {
	int sums = 0;
	for (int r = 1; r <= totalN; r++) {
		for (int c = 1; c <= totalN; c++) {
			if (arr[r][c]) sums += arr[r][c];
		}
	}
	return sums;
}
int FF(int sr, int sc) {
	static int dr[] = { -1,0,1,0 };
	static int dc[] = { 0,1,0,-1 };
	q = {};
	q.push({ sr,sc });
	int cnt = 1;
	ffVisit[sr][sc] = 1;
	while (!q.empty()) {
		POS data = q.front(); q.pop();
		for (int i = 0; i < 4; i++) {
			POS newdata = data;
			newdata.r += dr[i];
			newdata.c += dc[i];
			if (newdata.r<1 || newdata.c<1 || newdata.r>totalN || newdata.c>totalN) continue;
			if (ffVisit[newdata.r][newdata.c]) continue;
			if (!arr[newdata.r][newdata.c]) continue;
			ffVisit[newdata.r][newdata.c] = 1;
			q.push(newdata);
			cnt++;
		}
	}
	return cnt;
}
int countBigGroup() {
	int maxg = 0;
	fill(&ffVisit[0][0], &ffVisit[MAX_N + 1][MAX_N + 2], 0);
	for (int r = 1; r <= totalN; r++) {
		for (int c = 1; c <= totalN; c++) {
			if (!ffVisit[r][c] && arr[r][c]) {
				int ret = FF(r, c);
				if (ret > maxg) maxg = ret;
			}
		}
	}	
	return maxg;
}
void solve() {
	for (int i = 0; i < Q; i++) {
		cout << "before" << '\n';
		print();
		rotate(i);
		cout << "after" << '\n';
		print();
		firestorm();
	}
	sumIce = calcIceSum();
	maxgroup = countBigGroup();

	cout << sumIce << '\n' << maxgroup<< '\n';
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	solve();
	return 0;
}
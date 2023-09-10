#include <iostream>
#include <vector>

using namespace std;
int N, K, ans;
vector<vector<int>> R, M;
vector<int> cans;

void inputs() {
    cin >> N >> K;
    cans.resize(N);
    R.resize(K, vector<int>(N));
    M.resize(K, vector<int>(N));
    for (int i = 0; i < N; i++) {
        cin >> cans[i];
    }
    for (int i = 0; i < K; i++) {
        for (int j = 0; j < N; j++) {
            cin >> R[i][j];
        }
    }
    for (int i = 0; i < K; i++) {
        for (int j = 0; j < N; j++) {
            cin >> M[i][j];
        }
    }
}

void solve(int day, int rang, int marr) {
    if (day == K) {
        ans = max(ans, rang + marr);
        return;
    }
    for (int i = 0; i < N; i++) {
        int newrang = rang;
        int newmarr = marr;
        if (cans[i] > 0) {
            cans[i]--;
            newrang += R[day][i];
            for (int j = 0; j < N; j++) {
                if (cans[j] > 0) {
                    cans[j]--;
                    newmarr += M[day][j];
                    solve(day + 1, newrang, newmarr);
                    cans[j]++;
                    newmarr -= M[day][j];
                }
            }
            newrang -= R[day][i];
            cans[i]++;
        }
    }
}
int main() {
    inputs();
    solve(0, 0, 0);
    cout << ans << '\n';
    return 0;
}

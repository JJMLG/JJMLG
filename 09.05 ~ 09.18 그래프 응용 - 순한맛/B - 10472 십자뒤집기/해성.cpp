#include <iostream>
#include <vector>
#include <string>
//#include <queue>
using namespace std;
int P;
string board;
string whitepapper = "000000000";
string answers = "000000000";
int numbers[9];
vector<vector<pair<int, int>>> arr;
int maxx;
void inputData() 
{
	board = "000000000";
	whitepapper = "000000000";
	for (int i = 0; i < 9; i++)
	{	
		char cc; cin >> cc;
		if (cc == '.') board[i] = '0';
		else board[i] = '1';
	}
	maxx = 0xf777777;
}
int check() 
{
	answers = "000000000";
	int cnt = 0;
	static int dr[] = { -1,0,1,0 };
	static int dc[] = { 0,1,0,-1 };
	for (int i = 0; i < 9; i++)
	{
		if (whitepapper[i] == '1') 
		{
			cnt++;
			int y = i / 3;
			int x = i % 3;
			if (answers[y * 3 + x] == '0')  answers[y * 3 + x] = '1';
			else if (answers[y * 3 + x] == '1')  answers[y * 3 + x] = '0';
			for (int r = 0; r < 4; r++)
			{
				int dy = y + dr[r];
				int dx = x + dc[r];
				if (dy < 0 || dx < 0 || dy > 2 || dx > 2) continue;
				if (answers[dy * 3 + dx] == '0')  answers[dy * 3 + dx] = '1';
				else if (answers[dy * 3 + dx] == '1')  answers[dy * 3 + dx] = '0';
			}
		}
	}
	//cout << answers << " == " << board<<"\n";
	if (answers == board) return cnt;
	return 0;
}
void dfs(int dep) 
{
	if (dep == 9) 
	{
		//cout << whitepapper << "\n";
		int ans = check();
		//cout << ans<< '\n'; 
		if (ans && maxx > ans) maxx = ans;
		return;
	}
	for (int i = 0; i < 2; i++) 
	{
		whitepapper[dep] = '0'+ i;
		dfs(dep + 1);
		whitepapper[dep] = '0';
	}
}
int solve() 
{
	if (board == whitepapper) return 0;
	dfs(0);
	return maxx;
}
int main(void) 
{
	cin >> P;
	for (int i = 0; i < P; i++) 
	{
		inputData();
		int ans = solve();
		cout << ans;
	}
	return 0;

}

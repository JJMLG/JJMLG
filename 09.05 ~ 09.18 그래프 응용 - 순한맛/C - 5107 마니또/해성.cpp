#include <iostream>
#include <string>
#include <map>
using namespace std;
int N;
map<string, string> names;
map<string, int> visit;
int inputData() 
{
	cin >> N;
	if (!N) return 0;
	names.clear();
	visit.clear();
	for (int i = 0; i < N; i++) 
	{
		string from;
		string to;
		cin >> from >> to;
		names.insert({ from, to });
		visit.insert({ from, 0 });
	}
	return 1;
}
int DFS(string nowKey, string starter) 
{
	// 이미 방문한 사람이면 return
	if (visit.find(nowKey)->second) return 0;

	//방문처리
	visit.find(nowKey)->second = 1;
	//마니또를 받는 사람이 처음 연결고리의 시작이면 return 1;
	if ((names.find(nowKey)->second) == starter) return 1;
	
	// 연결고리가 되는 거면 DFS 끝내기;
	if (DFS(names.find(nowKey)->second, starter)) return 1;
	return 0;
}
int solve() 
{
	int cnt = 0;
	for (auto iter : names) 
	{
		string starter = iter.first;
		if (DFS(starter, starter)) cnt++;
	}
	return cnt;
}
int main(void) 
{
	int idx = 1;
	while (inputData()) 
	{
		cout<< idx << " " << solve() <<"\n";
		idx++;
	}
	return 0;
}
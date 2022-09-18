#include <iostream>
#include <queue>
using namespace std;
struct ST 
{
	int pos, cnt;
};

queue<ST> Q;
int A, B, N, M;
int visited[100000+1];
int BFS()
{
	if (N == M) return 0;
	Q.push({ N,0 });
	while (!Q.empty()) 
	{
		ST NOW = Q.front(); Q.pop();
		for (int i = 0; i < 8; i++) 
		{
			ST TEMP = NOW;
			TEMP.cnt += 1;
			switch (i)
			{
				case 0:	TEMP.pos += -1;	break;
				case 1:	TEMP.pos += 1;	break;
				case 2:	TEMP.pos += A;	break;
				case 3:	TEMP.pos -= A;	break;
				case 4:	TEMP.pos += B;	break;
				case 5:	TEMP.pos -= B;	break;
				case 6:	TEMP.pos *= A;	break;
				case 7:	TEMP.pos *= B;	break;
			}
			if (TEMP.pos < 0 || TEMP.pos>100000) continue;
			if (TEMP.pos == M) return TEMP.cnt;
			if (visited[TEMP.pos]) continue;
			visited[TEMP.pos] = 1;
			Q.push(TEMP);
		}
	}
}
int main(void) 
{
	cin >> A >> B >> N >> M;
	int ans = BFS();
	cout << ans << '\n';
	return 0;
}
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string A;
string B;
string ANT;
int a, b, T;
void input()
{
	cin >> a >> b;

	cin >> A;
	reverse(A.begin(), A.end());
	
	cin >> B;
	
	ANT = A + B;
	
	cin >> T;
}
void simulation()
{
	for (int t = 0; t < T; t++) {
		for (int i = 0; i < a+b-1; i++) {
			if (A.find(ANT[i]) != string::npos && B.find(ANT[i + 1]) != string::npos) 
			{
				swap(ANT[i], ANT[i+1]);
				i++;
			}
		}
	}
	cout << ANT;
}
int main(void)
{
	input();
	simulation();
	return 0;
}
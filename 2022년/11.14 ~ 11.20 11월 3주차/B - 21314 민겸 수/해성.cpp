#define _CRT_SECURE_NO_WARNINGS
#if 1
#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAX_N (3000+1)
string words;
vector<string> eachword;
int visit[MAX_N + 1];
int maxx, minn;
void input() {
	cin >> words;
}
string calc(string numb) {
	string result;
	//k가 있으면
	if (numb.find('K') != string::npos) {
		result.push_back('5');
		for (int i = 0; i < numb.size()-1; i++) {
			result.push_back('0');
		}
		//result = (long long)pow(10, numb.size() - 1) * 5;
	}
	else {
		result.push_back('1');
		for (int i = 0; i < numb.size() - 1; i++) {
			result.push_back('0');
		}
	}
	return result;
}
void solve() {
	string resultMax;
	string resultMin;
	string tempstr;

	for (int i = 0; i < words.size(); i++) {
		if (words[i] == 'M') {
			tempstr.push_back(words[i]);
		}
		//끝나고 tempstr 있는지 체크
		else if (words[i] == 'K') {
			//있었으면
			if (tempstr.size()) {
				resultMin += calc(tempstr) + '5';
			}
			else resultMin += '5';

			if (tempstr.find('K') != string::npos) {
				resultMax += calc(tempstr) + '5';
				tempstr.clear();
			}
			//없었으면
			else {
				tempstr.push_back(words[i]);
				resultMax += calc(tempstr);
				tempstr.clear();
			}
		}
	}
	if (tempstr.size()) {
		resultMax += calc(tempstr);
		resultMin += calc(tempstr);
	}
	
	if (words.find('K') == string::npos) {
		resultMax.clear();
		resultMin.clear();
		for (int i = 0; i < words.size(); i++) {
			resultMax += '1';
			resultMin += '0';
		}
		resultMin[0] = '1';
		
	}
	cout << resultMax << '\n' <<resultMin;

}
int main(void) {
	freopen("21314.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	input();
	solve();
}
#endif

#if 0
#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;
#define MAX_N (3000+1)

string words;
vector<string> eachword;
int visit[MAX_N + 1];
int maxx, minn;
void input() {
	cin >> words;
}
	if (temp[0] == ' ') return;
	if (dep == words.size()) {
		for (int i = 0; i < (int)temp.size()-1; i++) {
			if (temp[i] == 'K' && temp[i + 1] == 'K') return;
		}
		string spaces;
		vector<string> wordslist;
		for (int i = 0; i < (int)temp.size(); i++) {
			if (temp[i] == ' ') {
				wordslist.push_back(spaces);
				spaces.clear();
			}
			else {
				spaces += temp[i];
			}
		}
		if (spaces.size()) {
			wordslist.push_back(spaces);
			spaces.clear();
		}

		for (int i = 0; i < wordslist.size(); i++) {
			if (wordslist[i].size() > 1 && wordslist[i][0] == 'K') return;
			int kcnt = 0;
			for(int j =0; j < wordslist[i].size(); j++){
				if (wordslist[i][j] == 'K') kcnt++;
				if (kcnt >= 2) return;
			}
		}

		string sums;
		for (int i = 0; i < wordslist.size(); i++) {
			int temp = 0;
			int flag = 0;
			if (wordslist[i].find('K') != string::npos) { //k가 있으면
				flag = 1;
			}
			if (flag) { // k가 있으면
				for (int j = 0; j < wordslist[i].size(); j++) {
					temp = (int)pow(10, ((int)wordslist[i].size()-1))*5;
				}
			}
			else {
				for (int j = 0; j < wordslist[i].size(); j++) {
					temp = (int)pow(10, ((int)wordslist[i].size() - 1));
				}
			}
			sums += to_string(temp);
		}
		int result = stoi(sums);
		if (result > maxx) maxx = result;
		if (result < minn) minn = result;
		return;
	}

	dfs(dep + 1, temp + words[dep]);
	
	dfs(dep + 1, temp + " " + words[dep]);
}
void solve() {
	maxx = -1;
	minn = 0xf777777;
	dfs(0, "");
	cout << maxx << '\n' << minn;
	//cout << *(--numbers.end()) << '\n' << *numbers.begin();
}
int main(void) {
	freopen("21314.txt","r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	input();
	solve();
}
#endif
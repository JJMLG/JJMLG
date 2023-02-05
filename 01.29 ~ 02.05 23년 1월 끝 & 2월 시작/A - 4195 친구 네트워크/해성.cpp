#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <unordered_map>

using namespace std;

unordered_map<string, int> hashmap; // first: id, second: index
vector<int> parent, friend_num; // disjoint-set을 위한 배열, 연결된 친구가 몇 명인지 저장하는 변수


int getParent(int x) {
    if (parent[x] == x) return x;
    return parent[x] = getParent(parent[x]);
}

void unionParent(int a, int b) {
    a = getParent(a);
    b = getParent(b);

    // 수가 더 큰 쪽에 있는 친구의 수를, 수가 더 작은 쪽에 더한다
    if (a < b) {
        parent[b] = a;
        friend_num[a] += friend_num[b];
    }
    else if (a > b) {
        parent[a] = b;
        friend_num[b] += friend_num[a];
    }
}

void initParent(int num) {
    // 한 관계에 두 개의 id가 주어지기 때문에
    // 최대 사람 수는 (관계의 수) * 2 이다.
    parent.assign(num * 2 + 1, 0);
    friend_num.assign(num * 2 + 1, 1);

    for (int i = 0; i <= num * 2; i++) {
        parent[i] = i;
    }
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int testcase;

    cin >> testcase;
    while (testcase--) {
        hashmap.clear();
        int idx = 0, f = 0;

        cin >> f;
        initParent(f);

        // id_1의 인덱스 번호, id_2의 인덱스 번호
        int friend_n1 = 0, friend_n2 = 0;

        for (int i = 0; i < f; i++) {
            string id_1, id_2;
            cin >> id_1 >> id_2;

            // key id_1에 해당하는 value의 개수가 없을 때
            if (hashmap.count(id_1) == 0) {
                hashmap[id_1] = ++idx;
                friend_n1 = idx;
            }
            else { // 이미 존재한다면 key에 해당하는 value를 가지고 온다
                friend_n1 = hashmap[id_1];
            }

            if (hashmap.count(id_2) == 0) {
                hashmap[id_2] = ++idx;
                friend_n2 = idx;
            }
            else {
                friend_n2 = hashmap[id_2];
            }

            // unionParent를 통해 부모를 합친다.
            unionParent(friend_n1, friend_n2);
            int target = getParent(friend_n1);
            cout << friend_num[target] << '\n';
        }
    }

    return 0;
}
//#include <iostream>
//#include <unordered_map>
//#include <string>
//#include <set>
//using namespace std;
//unordered_map<string, set<string>> friends;
//int T, F;
//void init() {
//	friends.clear();
//}
//void input() {
//	cin >> F; 
//	for(int i=0; i<F;i++){
//		string A, B;
//		cin >> A >> B;
//		if (friends.find(A) != friends.end()) {
//			friends[A].insert(B);
//		}
//		else {
//			friends[A].insert({ A, B });
//		}
//		
//		if (friends.find(B) != friends.end()) {
//			friends[B].insert(A);
//		}
//		else {
//			friends[B].insert({ A, B });
//		}
//		cout << friends[A].size() << "\n";
//	}
//}
//int main(void) {
//	cin >> T;
//	for (int i = 0; i < T; i++) {
//		init();
//		input();
//	}
//	return 0;
//}

#include <iostream>
#include <vector>

#define ll long long

using namespace std;

int main() {
    int n, x;

    cin >> n >> x;

    vector<int> l;

    for (int i = 0; i < n; i++) {
        int m;

        cin >> m;

        if (m < x) {
            l.push_back(m);
        }
    }

    for (int i : l) {
        cout << i << " ";
    }



    return 0;
}

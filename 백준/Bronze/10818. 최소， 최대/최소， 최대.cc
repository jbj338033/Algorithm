#include <iostream>
#include <vector>

#define ll long long

using namespace std;

int min(vector<int> &v) {
    int min = 1000001;

    for (int i : v) {
        if (i < min) {
            min = i;
        }
    }

    return min;
}

int max(vector<int> &v) {
    int max = -1000001;

    for (int i : v) {
        if (i > max) {
            max = i;
        }
    }

    return max;
}

int main() {
    int n;

    cin >> n;

    vector<int> v;

    for (int i = 0; i < n; i++) {
        int a;

        cin >> a;

        v.push_back(a);
    }

    cout << min(v) << " " << max(v);

    return 0;
}

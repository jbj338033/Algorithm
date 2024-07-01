#include <iostream>

#define ll long long

using namespace std;

int main() {
    int n;

    cin >> n;

    int l[n];

    for (int i = 0; i < n; i++) {
        int a;

        cin >> a;

        l[i] = a;
    }

    int v;
    int count = 0;

    cin >> v;

    for (int i : l) {
        if (i == v) {
            count += 1;
        }
    }

    cout << count << "\n";

    return 0;
}

#include <iostream>

#define ll long long

using namespace std;

int main() {
    int t;

    cin >> t;

    for (int i = 0; i < t; i++) {
        int n;

        cin >> n;

        cout << (n % 2 == 0 ? "cubelover" : "koosaga") << "\n";
    }

    return 0;
}

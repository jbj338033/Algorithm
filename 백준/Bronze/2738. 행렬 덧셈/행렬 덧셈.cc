#include <iostream>

#define ll long long

using namespace std;

int main() {
    int n, m;

    cin >> n >> m;

    int a[n][m];
    int b[n][m];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> b[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << a[i][j] + b[i][j] << " ";
        }

        cout << "\n";
    }

    return 0;
}

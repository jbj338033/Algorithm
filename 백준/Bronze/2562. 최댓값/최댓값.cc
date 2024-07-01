#include <iostream>
#include <vector>

#define ll long long

using namespace std;

int main() {
    int l[9];

    for (int i = 0; i < 9; i++) {
        cin >> l[i];
    }

    int max = -1000001;
    int index = -1;

    for (int i = 0; i < 9; i++) {
        if (l[i] > max) {
            max = l[i];
            index = i + 1;
        }
    }

    cout << max << "\n" << index;

    return 0;
}
